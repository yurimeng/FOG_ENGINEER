"""CLI: python3.11 -m mdc_kb_reorg --root <MDC-KB>"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .inventory import write_inventory, snapshot
from .reorg import run_reorg
from .typesafe_client import MissingApiKeyError, redact


def default_root() -> Path:
    here = Path(__file__).resolve()
    # TOOLS/mdc_kb_reorg/__main__.py → MDC-KB
    cand = here.parents[2]
    if (cand / "KB").is_dir() and (cand / "Projects").is_dir():
        return cand
    cwd = Path.cwd()
    if (cwd / "KB").is_dir() and (cwd / "Projects").is_dir():
        return cwd
    return cand


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Reorganize MDC-KB into four domains; never delete.")
    parser.add_argument("--root", type=Path, default=None, help="MDC-KB root")
    parser.add_argument("--log-dir", type=Path, default=None)
    parser.add_argument("--max-typesafe", type=int, default=28)
    parser.add_argument("--skip-typesafe", action="store_true")
    parser.add_argument("--inventory-only", action="store_true")
    parser.add_argument(
        "--nav-only",
        action="store_true",
        help="Regenerate _domains pages only; do not apply 🧭 or rewrite block ids",
    )
    args = parser.parse_args(argv)

    root = (args.root or default_root()).resolve()
    if not root.is_dir():
        print(f"root not found: {root}", file=sys.stderr)
        return 2

    if args.inventory_only:
        recs = snapshot(root)
        if args.log_dir:
            args.log_dir.mkdir(parents=True, exist_ok=True)
            write_inventory(recs, args.log_dir / "inventory.txt")
        print(json.dumps({"root": str(root), "files": len(recs)}))
        return 0

    try:
        report = run_reorg(
            root,
            live_typesafe=not args.skip_typesafe,
            max_typesafe=args.max_typesafe,
            apply_moves=not args.nav_only,
            log_dir=args.log_dir,
            nav_only=args.nav_only,
        )
    except MissingApiKeyError as exc:
        print(redact(str(exc)), file=sys.stderr)
        return 2
    except Exception as exc:  # noqa: BLE001
        print(redact(f"{type(exc).__name__}: {exc}"), file=sys.stderr)
        return 1

    payload = {
        "ok": report.ok(),
        "root": report.root,
        "before_count": report.before_count,
        "after_count": report.after_count,
        "missing": report.missing,
        "domain_counts": report.domain_counts,
        "relocated": len(report.relocated),
        "typesafe_calls": report.typesafe_calls,
        "typed_used": report.typed_used,
        "checklist": report.checklist_path,
        "hub": report.hub_path,
        "smoke": report.smoke,
        "notes": report.exit_notes,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    print(redact(text))
    if args.log_dir:
        args.log_dir.mkdir(parents=True, exist_ok=True)
        (args.log_dir / "reorg-stdout.json").write_text(redact(text) + "\n", encoding="utf-8")
        write_inventory(snapshot(root), args.log_dir / "inventory-after.txt")
    return 0 if report.ok() else 1


if __name__ == "__main__":
    raise SystemExit(main())
