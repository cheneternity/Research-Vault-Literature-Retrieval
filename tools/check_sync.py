"""Fail when the standalone release diverges from its canonical Skill source."""
from __future__ import annotations

import argparse
from pathlib import Path

FILES = ("SKILL.md", "agents/openai.yaml", "references/retrieval-routing.md")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canonical-dir", type=Path, required=True)
    parser.add_argument("--mirror-dir", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    failed = False
    for relative in FILES:
        canonical, mirror = args.canonical_dir / relative, args.mirror_dir / relative
        if not canonical.is_file() or not mirror.is_file():
            print(f"FAIL: missing {relative}")
            failed = True
        elif canonical.read_bytes() != mirror.read_bytes():
            print(f"FAIL: drift in {relative}")
            failed = True
    print("RESULT: FAIL" if failed else "RESULT: PASS; mirror matches canonical Retrieval Skill")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
