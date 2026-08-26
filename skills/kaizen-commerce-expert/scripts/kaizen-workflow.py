#!/usr/bin/env python3
"""Runtime wrapper for the repo-level Kai workflow dispatcher."""

from __future__ import annotations

import os
import sys
from pathlib import Path


SCRIPT_NAME = "kaizen-workflow.py"
DEFAULT_SOURCE_ROOT = Path.home() / "Documents" / "Codex" / "kaizen-skills"


def _candidate_roots() -> list[Path]:
    here = Path(__file__).resolve()
    roots: list[Path] = []

    env_root = os.environ.get("KAIZEN_SKILLS_ROOT") or os.environ.get("KAI_SOURCE_ROOT")
    if env_root:
        roots.append(Path(env_root).expanduser())

    # Source checkout layout: skills/kaizen-commerce-expert/scripts/<wrapper>.
    roots.append(here.parents[3])
    roots.append(DEFAULT_SOURCE_ROOT)

    seen: set[Path] = set()
    unique: list[Path] = []
    for root in roots:
        resolved = root.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return unique


def _resolve_target() -> Path:
    here = Path(__file__).resolve()
    for root in _candidate_roots():
        target = root / "scripts" / SCRIPT_NAME
        if target.exists() and target.resolve() != here:
            return target
    searched = "\n".join(f"- {root / 'scripts' / SCRIPT_NAME}" for root in _candidate_roots())
    raise SystemExit(
        "Cannot find the repo-level Kai workflow dispatcher.\n"
        "Set KAIZEN_SKILLS_ROOT to the kaizen-skills checkout.\n"
        f"Searched:\n{searched}"
    )


def main() -> None:
    target = _resolve_target()
    os.execv(sys.executable, [sys.executable, str(target), *sys.argv[1:]])


if __name__ == "__main__":
    main()
