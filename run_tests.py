from __future__ import annotations

__all__: list[str] = []

import sys

import gravy.tests


def main() -> int:
    return int(not gravy.tests.test().wasSuccessful())


if __name__ == "__main__":
    sys.exit(main())
