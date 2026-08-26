#!/usr/bin/env python3
"""Audit KaizenCommerce proposal artifacts against the kaizen-propose protocol."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "Situation",
    "Our Recommendation",
    "Scope of Work",
    "Recommended App and Platform Stack",
    "Business Case",
    "Migration and Implementation Approach",
    "Technical SEO Migration",
    "Go-Live and Hypercare",
    "Risk Register",
    "Timeline",
    "Risks and Assumptions",
    "Investment",
    "Payment Schedule",
    "Why KaizenCommerce",
    "Next Steps",
]

FORBIDDEN_PATTERNS = [
    r"we are pleased to present",
    r"as discussed",
    r"please don't hesitate",
    r"\bour team\b",
    r"world-class",
    r"best-in-class",
    r"cutting-edge",
    r"seamlessly",
    r"\bleverage\b",
    r"\brobust\b",
    r"\bscalable\b",
    r"one-stop shop",
    r"it is recommended that",
    r"in today's landscape",
    r"now more than ever",
]

INTERNAL_PACKAGE_PATTERNS = [
    r"\bSilver\b",
    r"\bGold\b",
    r"\bDiamond\b",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text()


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def find_pattern_hits(text: str, patterns: list[str]) -> list[str]:
    hits: list[str] = []
    for pattern in patterns:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            hits.append(f"line {line_number(text, match.start())}: {match.group(0)!r}")
    return hits


def audit_markdown(path: Path) -> list[str]:
    text = read_text(path)
    failures: list[str] = []

    headings = re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE)
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in headings]
    if missing:
        failures.append("missing required headings: " + ", ".join(missing))

    forbidden = find_pattern_hits(text, FORBIDDEN_PATTERNS)
    if forbidden:
        failures.append("forbidden voice/package phrases found: " + "; ".join(forbidden))

    package_hits = find_pattern_hits(text, INTERNAL_PACKAGE_PATTERNS)
    if package_hits:
        failures.append("client-facing internal package names found: " + "; ".join(package_hits))

    required_phrases = [
        "Blueprint credit",
        "Net implementation investment",
        "Payment Schedule",
        "14 calendar days",
        "App, platform, connector, and vendor costs are billed directly",
        "The Kaizen Cutover",
    ]
    missing_phrases = [phrase for phrase in required_phrases if phrase not in text]
    if missing_phrases:
        failures.append("missing required commercial/protocol phrases: " + ", ".join(missing_phrases))

    if text.count("|---") < 8:
        failures.append("proposal appears to have too few structured tables for the required format")

    return failures


def audit_internal_qa(path: Path) -> list[str]:
    text = read_text(path)
    failures: list[str] = []
    for phrase in ["Win Theme Matrix", "SCQA", "Three-Act Narrative Check"]:
        if phrase not in text:
            failures.append(f"internal QA artifact missing {phrase!r}")
    return failures


def audit_pdf(path: Path) -> list[str]:
    failures: list[str] = []
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return ["pypdf unavailable; cannot verify PDF page count or empty pages"]

    reader = PdfReader(str(path))
    page_count = len(reader.pages)
    if page_count < 8 or page_count > 11:
        failures.append(f"PDF page count is {page_count}; expected 8-11")

    short_pages: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        compact = " ".join((page.extract_text() or "").split())
        if index == 1:
            continue
        if len(compact) < 700:
            short_pages.append(f"{index} ({len(compact)} chars)")
    if short_pages:
        failures.append("near-empty body pages found: " + ", ".join(short_pages))

    return failures


def run(args: argparse.Namespace) -> int:
    failures: list[str] = []

    markdown = Path(args.markdown)
    if not markdown.exists():
        failures.append(f"markdown not found: {markdown}")
    else:
        failures.extend(audit_markdown(markdown))

    if args.internal_qa:
        qa = Path(args.internal_qa)
        if not qa.exists():
            failures.append(f"internal QA artifact not found: {qa}")
        else:
            failures.extend(audit_internal_qa(qa))

    if args.pdf:
        pdf = Path(args.pdf)
        if not pdf.exists():
            failures.append(f"PDF not found: {pdf}")
        else:
            failures.extend(audit_pdf(pdf))

    if failures:
        print("Proposal protocol audit failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Proposal protocol audit passed.")
    return 0


def self_test() -> int:
    sample = "\n".join(f"## {heading}" for heading in REQUIRED_HEADINGS)
    sample += """

Blueprint credit
Net implementation investment
Payment Schedule
14 calendar days
App, platform, connector, and vendor costs are billed directly
The Kaizen Cutover

| A | B |
|---|---|
| 1 | 2 |
| A | B |
|---|---|
| 1 | 2 |
| A | B |
|---|---|
| 1 | 2 |
| A | B |
|---|---|
| 1 | 2 |
| A | B |
|---|---|
| 1 | 2 |
| A | B |
|---|---|
| 1 | 2 |
| A | B |
|---|---|
| 1 | 2 |
| A | B |
|---|---|
| 1 | 2 |
"""
    tmp = Path("/tmp/kaizen-proposal-audit-self-test.md")
    tmp.write_text(sample, encoding="utf-8")
    failures = audit_markdown(tmp)
    if failures:
        print("Self-test failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Self-test passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", nargs="?")
    parser.add_argument("--pdf")
    parser.add_argument("--internal-qa")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.markdown:
        parser.error("markdown path is required unless --self-test is used")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
