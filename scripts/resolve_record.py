# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import argparse

from arrlib import ROOT, discover_papers, select_paper


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve an ARR record version to its source directory.")
    parser.add_argument("paper_id")
    parser.add_argument("--version", default="")
    parser.add_argument("--field", choices=("path", "version"), default="path")
    args = parser.parse_args()
    paper = select_paper(discover_papers(), args.paper_id, args.version or None)
    print(paper.path.relative_to(ROOT) if args.field == "path" else paper.version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
