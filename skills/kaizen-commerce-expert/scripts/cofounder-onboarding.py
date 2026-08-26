#!/usr/bin/env python3
"""Track cofounder onboarding locally without ever storing credentials."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import tempfile


STEPS = (
    "operator_profile",
    "skill_discovery",
    "personal_agent_key",
    "mcp_connection",
    "read_check",
    "dry_run_check",
    "attribution_check",
)


def state_path() -> Path:
    return Path(os.environ.get("KAI_ONBOARDING_STATE", "~/.kaizen/cofounder-onboarding.json")).expanduser()


def load() -> dict:
    path = state_path()
    if not path.exists():
        return {"version": 1, "runtime": None, "steps": {step: False for step in STEPS}}
    data = json.loads(path.read_text())
    data.setdefault("version", 1)
    data.setdefault("runtime", None)
    saved_steps = data.setdefault("steps", {})
    for step in STEPS:
        saved_steps.setdefault(step, False)
    return data


def save(data: dict) -> None:
    path = state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.chmod(temporary, 0o600)
        os.replace(temporary, path)
        os.chmod(path, 0o600)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init")
    init.add_argument("--runtime", choices=("claude", "gemini"), required=True)

    complete = subparsers.add_parser("complete")
    complete.add_argument("step", choices=STEPS)

    subparsers.add_parser("status")
    args = parser.parse_args()

    data = load()
    if args.command == "init":
        if data["runtime"] not in (None, args.runtime):
            raise SystemExit(
                f"Onboarding already belongs to runtime {data['runtime']}; "
                "preserving it. Set KAI_ONBOARDING_STATE to use a separate state file."
            )
        data["runtime"] = args.runtime
        save(data)
    elif args.command == "complete":
        data["steps"][args.step] = True
        save(data)

    completed = sum(bool(data["steps"][step]) for step in STEPS)
    print(f"Kai cofounder onboarding: {completed}/{len(STEPS)} complete")
    print(f"Runtime: {data['runtime'] or 'not set'}")
    for step in STEPS:
        marker = "x" if data["steps"][step] else " "
        print(f"[{marker}] {step}")
    print(f"State: {state_path()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
