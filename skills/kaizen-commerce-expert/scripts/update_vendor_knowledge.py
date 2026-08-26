#!/usr/bin/env python3
"""Update Kai's generated vendor freshness index.

This script intentionally keeps the local index conservative. It collects recent Shopify and
AnyDB changes, routes them to generated navigation notes, and flags ambiguous entries for human
merge instead of silently changing Kai's canonical judgment rules.
"""

from __future__ import annotations

import argparse
import email.utils
import html
import html.parser
import json
import re
import sys
import textwrap
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import vendor_queue  # noqa: E402

CONTENT_ROOT = SKILL_ROOT / "reference-content"
STATE_PATH = CONTENT_ROOT / "_changelog-state.json"
MANIFEST_PATH = CONTENT_ROOT / "_freshness-manifest.json"
NEEDS_MERGE_PATH = CONTENT_ROOT / "_needs-merge.md"
ROUTING_PATH = Path(__file__).with_name("changelog_routing.json")

SHOPIFY_MERCHANT_FEED = "https://changelog.shopify.com/feed.xml"
SHOPIFY_DEV_FEED = "https://shopify.dev/changelog/feed.xml"
ANYDB_RELEASES_JSON = "https://www.anydb.com/community/c/releases/6.json"
ANYDB_RELEASES_URL = "https://www.anydb.com/community/c/releases/6"
ANYDB_ROADMAP_URL = "https://www.anydb.com/support/roadmap/"
ANYDB_RELEASENOTES_URL = "https://www.anydb.com/support/releasenotes/"

SOURCE_LABELS = {
    "shopify-help": "Shopify merchant changelog",
    "shopify-dev": "Shopify developer changelog",
    "anydb": "AnyDB releases and roadmap",
}


@dataclass
class Entry:
    source: str
    title: str
    url: str
    published_at: datetime
    summary: str
    categories: list[str]

    @property
    def key(self) -> str:
        return f"{self.source}:{self.url or self.title}"

    @property
    def haystack(self) -> str:
        return " ".join([self.title, self.summary, " ".join(self.categories)]).lower()


@dataclass
class RoutedEntry:
    entry: Entry
    section: str
    label: str
    auto_edit: bool
    needs_merge: bool
    reason: str


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_dt(value: str | None) -> datetime:
    if not value:
        return datetime.fromtimestamp(0, timezone.utc)
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError):
        pass
    try:
        normalized = value.replace("Z", "+00:00")
        parsed = datetime.fromisoformat(normalized)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return datetime.fromtimestamp(0, timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def fetch_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "KaiVendorFreshness/1.0 (+https://github.com/Kaizen-Commerce/kaizen-skills)",
            "Accept": "application/rss+xml, application/json, text/html;q=0.9, */*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


# Characters XML 1.0 forbids anywhere in a document, including inside CDATA:
# everything outside #x9 | #xA | #xD | #x20-#xD7FF | #xE000-#xFFFD | #x10000-#x10FFFF.
# Publishers emit these by accident (a stray control character pasted into a code
# block), and one of them anywhere in a multi-megabyte feed makes the whole document
# unparseable, which silently costs a full sync window. Strip them before parsing.
_ILLEGAL_XML_CHARS = re.compile(
    "[^\x09\x0a\x0d\x20-퟿-�\U00010000-\U0010ffff]"
)


def sanitize_xml(raw: str) -> tuple[str, int]:
    """Drop characters XML 1.0 forbids. Returns the cleaned text and how many were removed."""
    cleaned, removed = _ILLEGAL_XML_CHARS.subn("", raw)
    return cleaned, removed


def strip_html(raw: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", raw or "", flags=re.I)
    text = re.sub(r"</p\s*>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return ascii_text(text)


def ascii_text(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2026": "...",
        "\u00a0": " ",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


_RELEASENOTES_DATE_RE = re.compile(
    r"\b(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
    r"Dec(?:ember)?)\s+\d{1,2},?\s+\d{4}\b",
    re.I,
)


class _ReleaseNotesHTMLParser(html.parser.HTMLParser):
    """Extract dated release sections from the AnyDB release notes page."""

    def __init__(self) -> None:
        super().__init__()
        self._in_heading = False
        self._heading_buf = ""
        self._in_li = False
        self._li_buf = ""
        self._current_section: dict[str, Any] | None = None
        self.sections: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[Any]) -> None:
        if tag in ("h2", "h3", "h4", "h5", "h6"):
            self._in_heading = True
            self._heading_buf = ""
        elif tag == "li":
            self._in_li = True
            self._li_buf = ""

    def handle_endtag(self, tag: str) -> None:
        if tag in ("h2", "h3", "h4", "h5", "h6"):
            self._in_heading = False
            text = self._heading_buf.strip()
            if _RELEASENOTES_DATE_RE.search(text):
                self._current_section = {"heading": text, "bullets": []}
                self.sections.append(self._current_section)
        elif tag == "li":
            self._in_li = False
            text = self._li_buf.strip()
            if text and self._current_section is not None:
                self._current_section["bullets"].append(text)
            self._li_buf = ""

    def handle_data(self, data: str) -> None:
        if self._in_heading:
            self._heading_buf += data
        elif self._in_li:
            self._li_buf += data


def _parse_releasenotes_date(date_str: str) -> datetime | None:
    date_str = date_str.strip()
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%b %Y", "%B %Y"):
        try:
            return datetime.strptime(date_str, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def truncate(text: str, limit: int = 420) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def load_state() -> dict[str, Any]:
    return load_json(
        STATE_PATH,
        {
            "version": 1,
            "last_fetch": None,
            "seen_entries": {},
            "sources": {},
        },
    )


def load_routing() -> dict[str, Any]:
    return load_json(ROUTING_PATH, {"routes": [], "ambiguous_keywords": []})


def fetch_rss_entries(source: str, url: str) -> list[Entry]:
    raw = fetch_text(url)
    cleaned, removed = sanitize_xml(raw)
    if removed:
        print(
            f"  note: stripped {removed} illegal XML character(s) from {source} feed before parsing",
            file=sys.stderr,
        )
    root = ET.fromstring(cleaned)
    entries: list[Entry] = []
    for item in root.findall(".//item"):
        title = ascii_text((item.findtext("title") or "").strip())
        link = (item.findtext("link") or "").strip()
        summary = strip_html(item.findtext("description") or "")
        published = parse_dt(item.findtext("pubDate"))
        categories = [ascii_text((cat.text or "").strip()) for cat in item.findall("category") if (cat.text or "").strip()]
        if title:
            entries.append(
                Entry(
                    source=source,
                    title=title,
                    url=link,
                    published_at=published,
                    summary=summary,
                    categories=categories,
                )
            )
    return entries


def fetch_anydb_entries() -> list[Entry]:
    raw = fetch_text(ANYDB_RELEASES_JSON)
    data = json.loads(raw)
    entries: list[Entry] = []
    for topic in data.get("topic_list", {}).get("topics", []):
        title = strip_html(topic.get("title") or topic.get("fancy_title") or "")
        if not title or title.lower().startswith("about the releases category"):
            continue
        slug = topic.get("slug")
        topic_id = topic.get("id")
        url = f"https://www.anydb.com/community/t/{slug}/{topic_id}" if slug and topic_id else ANYDB_RELEASES_URL
        summary = strip_html(topic.get("excerpt") or "")
        published = parse_dt(topic.get("created_at") or topic.get("last_posted_at"))
        entries.append(
            Entry(
                source="anydb",
                title=title,
                url=url,
                published_at=published,
                summary=summary,
                categories=["AnyDB", "Release"],
            )
        )
    entries.append(
        Entry(
            source="anydb",
            title="AnyDB roadmap",
            url=ANYDB_ROADMAP_URL,
            published_at=now_utc(),
            summary="Public roadmap surface. Treat roadmap items as directional until release notes or docs confirm shipped behavior.",
            categories=["AnyDB", "Roadmap"],
        )
    )
    return entries


def fetch_anydb_releasenotes_entries() -> list[Entry]:
    """Fetch and parse the AnyDB official release notes page."""
    raw = fetch_text(ANYDB_RELEASENOTES_URL)
    parser = _ReleaseNotesHTMLParser()
    parser.feed(raw)

    entries: list[Entry] = []
    for section in parser.sections:
        heading = ascii_text(str(section["heading"]))
        bullets: list[str] = [ascii_text(str(b)) for b in section.get("bullets", [])]

        date_match = _RELEASENOTES_DATE_RE.search(heading)
        if not date_match:
            continue
        date_str = date_match.group(0)
        dt = _parse_releasenotes_date(date_str)
        if dt is None:
            continue

        summary_parts = bullets[:5]
        summary = "; ".join(summary_parts)
        if len(bullets) > 5:
            summary += f" [+{len(bullets) - 5} more]"

        anchor = re.sub(r"[^a-z0-9]+", "-", date_str.lower()).strip("-")
        url = f"{ANYDB_RELEASENOTES_URL}#{anchor}"

        entries.append(
            Entry(
                source="anydb",
                title=f"AnyDB Release Notes - {date_str}",
                url=url,
                published_at=dt,
                summary=truncate(summary or "Release notes entry."),
                categories=["AnyDB", "Release Notes"],
            )
        )
    return entries


# Entry.source values, and which fetcher keys must all succeed for that source to count
# as healthy. anydb is fed by two fetchers, so one failing holds the whole source back.
SOURCE_FETCHERS = {
    "shopify-help": ("shopify-help",),
    "shopify-dev": ("shopify-dev",),
    "anydb": ("anydb", "anydb-releasenotes"),
}


def since_cutoff(state: dict[str, Any], lookback_days: int, source: str | None = None) -> datetime:
    """Cutoff for a source, preferring its own last successful fetch.

    A single global cutoff loses data: while one source is failing, the others keep
    advancing the shared timestamp, so everything the broken source published during the
    outage falls behind the cutoff and is never ingested once it recovers. Each source
    therefore carries its own timestamp, advanced only on a run where that source
    succeeded. Falls back to the legacy global value for states written before this.
    """
    if source:
        per_source = (state.get("last_fetch_by_source") or {}).get(source)
        if per_source:
            return parse_dt(per_source) - timedelta(minutes=5)
    last_fetch = state.get("last_fetch")
    if last_fetch:
        return parse_dt(last_fetch) - timedelta(minutes=5)
    return now_utc() - timedelta(days=lookback_days)


def healthy_sources(errors: dict[str, str]) -> set[str]:
    """Entry.source values whose every backing fetcher succeeded this run."""
    return {
        source
        for source, fetchers in SOURCE_FETCHERS.items()
        if not any(key in errors for key in fetchers)
    }


def route_entry(entry: Entry, routing: dict[str, Any]) -> RoutedEntry:
    routes = routing.get("routes", [])
    ambiguous_keywords = routing.get("ambiguous_keywords", [])
    title_and_categories = " ".join([entry.title, " ".join(entry.categories)]).lower()
    summary = entry.summary.lower()
    best: dict[str, Any] | None = None
    best_score = 0
    for route in routes:
        if route.get("source_family") != entry.source:
            continue
        score = 0
        for keyword in route.get("keywords", []):
            if keyword_matches(keyword, title_and_categories):
                score += 2
            elif keyword_matches(keyword, summary):
                score += 1
        if score > best_score:
            best = route
            best_score = score
    if best is None:
        fallback = {
            "section": f"{entry.source}/general",
            "label": SOURCE_LABELS.get(entry.source, entry.source),
            "auto_edit": False,
        }
        best = fallback

    matched_ambiguous = [word for word in ambiguous_keywords if word in entry.haystack]
    needs_merge = bool(matched_ambiguous) or not bool(best.get("auto_edit"))
    if matched_ambiguous:
        reason = "ambiguous terms: " + ", ".join(matched_ambiguous[:5])
    elif not bool(best.get("auto_edit")):
        reason = "review required by route"
    else:
        reason = "auto-curated route"
    return RoutedEntry(
        entry=entry,
        section=best["section"],
        label=best.get("label", best["section"]),
        auto_edit=bool(best.get("auto_edit")) and not needs_merge,
        needs_merge=needs_merge,
        reason=reason,
    )


def keyword_matches(keyword: str, haystack: str) -> bool:
    keyword = keyword.lower().strip()
    if not keyword:
        return False
    if re.search(r"[^a-z0-9_-]", keyword):
        return keyword in haystack
    return bool(re.search(rf"\b{re.escape(keyword)}\b", haystack))


def group_by_section(items: list[RoutedEntry]) -> dict[str, list[RoutedEntry]]:
    grouped: dict[str, list[RoutedEntry]] = {}
    for item in items:
        grouped.setdefault(item.section, []).append(item)
    for section_items in grouped.values():
        section_items.sort(key=lambda routed: routed.entry.published_at, reverse=True)
    return grouped


def entry_bullet(item: RoutedEntry) -> str:
    status = "AUTO-CURATED" if item.auto_edit else "NEEDS-MERGE"
    date = item.entry.published_at.date().isoformat()
    categories = ", ".join(item.entry.categories) if item.entry.categories else "uncategorized"
    summary = truncate(item.entry.summary)
    return textwrap.dedent(
        f"""\
        - [{status}] {date} - [{item.entry.title}]({item.entry.url})
          - Source: {SOURCE_LABELS.get(item.entry.source, item.entry.source)}; route: {item.label}; categories: {categories}
          - Note: {summary or "No summary provided by source."}
          - Freshness rule: validate canonical vendor docs/MCP before production guidance.
        """
    )


def write_feed(path: Path, title: str, source_note: str, items: list[RoutedEntry]) -> None:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    existing_entries = existing if existing else ""
    new_block = "\n".join(entry_bullet(item).rstrip() for item in items).strip()
    if not existing:
        content = f"# {title}\n\n{source_note}\n\n"
    else:
        content = existing_entries.rstrip() + "\n\n"
    if new_block:
        content += f"## Update run - {now_utc().date().isoformat()}\n\n{new_block}\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def build_canonical_content(section: str, label: str, items: list[RoutedEntry]) -> str:
    generated = "\n".join(entry_bullet(item).rstrip() for item in items if item.auto_edit).strip()
    if not generated:
        generated = "- No auto-curated updates yet. Check the feed and canonical vendor docs before relying on local notes."
    return (
        f"# {label}\n\n"
        "Generated Kai vendor freshness note. Use this file for navigation and recent-change awareness only.\n"
        "Validate current behavior through the canonical vendor source before production guidance.\n\n"
        "## Recent feature updates (auto-curated)\n\n"
        "<!-- BEGIN AUTO-CURATED UPDATES -->\n"
        f"{generated}\n"
        "<!-- END AUTO-CURATED UPDATES -->\n\n"
        "## Canonical validation rule\n\n"
        "- Shopify developer/API behavior: validate through Shopify Dev MCP and `shopify.dev`.\n"
        "- Shopify merchant/admin behavior: validate against `help.shopify.com`, `changelog.shopify.com`, or live Admin evidence where available.\n"
        "- AnyDB behavior: validate against AnyDB MCP/docs and public release notes before build-ready artifacts.\n"
    )


def write_canonical(path: Path, section: str, label: str, items: list[RoutedEntry]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        new_block = "\n".join(
            entry_bullet(item).rstrip() for item in items if item.auto_edit
        ).strip()
        content = vendor_queue.append_auto_curated(
            path.read_text(encoding="utf-8"),
            new_block,
        )
    else:
        content = build_canonical_content(section, label, items)
    path.write_text(content, encoding="utf-8")


def write_readme() -> None:
    readme = CONTENT_ROOT / "README.md"
    readme.write_text(
        textwrap.dedent(
            """\
            # Kai Vendor Freshness Index

            This directory is generated by `scripts/update_vendor_knowledge.py`.

            It is a navigation layer for current Shopify and AnyDB changes, not the final source
            of truth. Kai must still validate current Shopify technical behavior through Shopify
            Dev MCP and AnyDB behavior through AnyDB docs/MCP before production guidance.

            Generated files:

            - `_freshness-manifest.json` - last update summary and source status.
            - `_changelog-state.json` - dedupe and review lifecycle state.
            - `_needs-merge.md` - regenerated pending/blocked review queue.
            - `shopify-dev/` - Shopify developer changelog routing notes.
            - `shopify-help/` - Shopify merchant changelog routing notes.
            - `anydb/` - AnyDB release and roadmap routing notes.

            Review lifecycle:

            - New ambiguous items enter as `pending_review`.
            - Reviewed items become `merged`, `archived`, or `blocked`.
            - Apply reviewed decisions with `scripts/curate_vendor_knowledge.py --decisions <file>`.
            - The queue is regenerated from state, so resolved items do not accumulate.
            """
        ),
        encoding="utf-8",
    )


def collect_entries() -> tuple[list[Entry], dict[str, str]]:
    errors: dict[str, str] = {}
    all_entries: list[Entry] = []
    sources = [
        ("shopify-help", SHOPIFY_MERCHANT_FEED, fetch_rss_entries),
        ("shopify-dev", SHOPIFY_DEV_FEED, fetch_rss_entries),
    ]
    for source, url, fetcher in sources:
        try:
            all_entries.extend(fetcher(source, url))
        except (urllib.error.URLError, ET.ParseError, TimeoutError) as exc:
            errors[source] = str(exc)
    try:
        all_entries.extend(fetch_anydb_entries())
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as exc:
        errors["anydb"] = str(exc)
    try:
        all_entries.extend(fetch_anydb_releasenotes_entries())
    except (urllib.error.URLError, TimeoutError) as exc:
        errors["anydb-releasenotes"] = str(exc)
    return all_entries, errors


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Update Kai vendor freshness index")
    parser.add_argument("--lookback-days", type=int, default=30, help="First-run lookback window")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and report without writing files")
    parser.add_argument(
        "--backfill",
        action="append",
        default=[],
        choices=sorted(SOURCE_FETCHERS),
        help=(
            "Ignore the stored timestamp for this source and rescan the full --lookback-days "
            "window. Use after a source has been failing, to recover what it missed. "
            "Repeatable. Already-seen entries stay deduped."
        ),
    )
    args = parser.parse_args(argv)

    CONTENT_ROOT.mkdir(parents=True, exist_ok=True)
    state = load_state()
    vendor_queue.normalize_state(state)
    routing = load_routing()
    cutoff = since_cutoff(state, args.lookback_days)
    seen = dict(state.get("seen_entries", {}))

    entries, errors = collect_entries()
    backfill = set(args.backfill)
    cutoffs = {
        source: (
            now_utc() - timedelta(days=args.lookback_days)
            if source in backfill
            else since_cutoff(state, args.lookback_days, source)
        )
        for source in SOURCE_FETCHERS
    }
    for source in sorted(backfill):
        print(f"  backfilling {source} from {iso(cutoffs[source])}", file=sys.stderr)
    candidates = [
        entry
        for entry in entries
        if entry.published_at >= cutoffs.get(entry.source, cutoff) and entry.key not in seen
    ]
    candidates.sort(key=lambda entry: entry.published_at, reverse=True)
    routed = [route_entry(entry, routing) for entry in candidates]

    if args.dry_run:
        print(f"Fetched entries: {len(entries)}")
        print(f"New entries: {len(routed)}")
        for source in sorted(cutoffs):
            print(f"  cutoff {source}: {iso(cutoffs[source])}")
        print(f"Needs merge: {sum(1 for item in routed if item.needs_merge)}")
        for item in routed[:20]:
            print(f"- {item.section}: {item.entry.title} ({item.reason})")
        if errors:
            print("Errors:")
            for source, error in errors.items():
                print(f"- {source}: {error}")
        return 0 if not errors else 1

    grouped = group_by_section(routed)
    by_source: dict[str, list[RoutedEntry]] = {}
    for item in routed:
        by_source.setdefault(item.entry.source, []).append(item)

    for source, items in by_source.items():
        source_dir = CONTENT_ROOT / source
        write_feed(
            source_dir / "_changelog-feed.md",
            f"{SOURCE_LABELS.get(source, source)} feed",
            "Generated from canonical vendor change surfaces. Validate live before production guidance.",
            items,
        )

    for section, items in grouped.items():
        auto_items = [item for item in items if item.auto_edit]
        label = items[0].label if items else section
        if auto_items:
            write_canonical(CONTENT_ROOT / f"{section}.md", section, label, items)

    write_readme()

    fetched_at = now_utc()
    for item in routed:
        seen[item.entry.key] = {
            "title": item.entry.title,
            "source": item.entry.source,
            "url": item.entry.url,
            "published_at": iso(item.entry.published_at),
            "section": item.section,
            "needs_merge": item.needs_merge,
            "status": "pending_review" if item.needs_merge else "auto_curated",
            "review_reason": item.reason,
            "summary": item.entry.summary,
            "categories": item.entry.categories,
        }
    # Advance only the sources that actually succeeded. A failed source keeps its previous
    # timestamp so its backlog is still in range on the run where it recovers.
    last_fetch_by_source = dict(state.get("last_fetch_by_source") or {})
    for source in healthy_sources(errors):
        last_fetch_by_source[source] = iso(fetched_at)

    state.update(
        {
            "version": 1,
            "last_fetch": iso(fetched_at),
            "last_fetch_by_source": last_fetch_by_source,
            "seen_entries": seen,
            "sources": {
                "shopify-help": SHOPIFY_MERCHANT_FEED,
                "shopify-dev": SHOPIFY_DEV_FEED,
                "anydb-releases": ANYDB_RELEASES_JSON,
                "anydb-roadmap": ANYDB_ROADMAP_URL,
                "anydb-releasenotes": ANYDB_RELEASENOTES_URL,
            },
        }
    )
    write_json(STATE_PATH, state)
    vendor_queue.write_queue(state, NEEDS_MERGE_PATH)

    manifest = {
        "version": 1,
        "generated_at": iso(fetched_at),
        "lookback_cutoff": iso(cutoff),
        "cutoffs_by_source": {source: iso(value) for source, value in sorted(cutoffs.items())},
        "new_entries": len(routed),
        "needs_merge": vendor_queue.unresolved_count(state),
        "reviewed_merged": sum(
            1 for entry in state["seen_entries"].values()
            if vendor_queue.entry_status(entry) == "merged"
        ),
        "reviewed_archived": sum(
            1 for entry in state["seen_entries"].values()
            if vendor_queue.entry_status(entry) == "archived"
        ),
        "blocked": sum(
            1 for entry in state["seen_entries"].values()
            if vendor_queue.entry_status(entry) == "blocked"
        ),
        "auto_curated": sum(1 for item in routed if item.auto_edit),
        "sections_updated": sorted(grouped),
        "errors": errors,
        "source_urls": {
            "shopify_merchant_changelog": SHOPIFY_MERCHANT_FEED,
            "shopify_developer_changelog": SHOPIFY_DEV_FEED,
            "anydb_releases": ANYDB_RELEASES_URL,
            "anydb_releases_json": ANYDB_RELEASES_JSON,
            "anydb_roadmap": ANYDB_ROADMAP_URL,
            "anydb_releasenotes": ANYDB_RELEASENOTES_URL,
        },
    }
    write_json(MANIFEST_PATH, manifest)

    print(f"Vendor freshness update complete: {len(routed)} new entries")
    print(f"Auto-curated: {manifest['auto_curated']}")
    print(f"Needs merge: {manifest['needs_merge']}")
    if errors:
        print("Source errors:")
        for source, error in errors.items():
            print(f"- {source}: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
