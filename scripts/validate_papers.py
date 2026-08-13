# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import sys

from arrlib import discover_papers, validate_collection


def main() -> int:
    papers = discover_papers()
    failures = validate_collection(papers)
    if failures:
        print("ARR validation failed:")
        for path, errors in failures.items():
            print(f"\n{path}")
            for error in errors:
                print(f"  - {error}")
        return 1
    print(f"ARR validation passed ({len(papers)} published paper(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
