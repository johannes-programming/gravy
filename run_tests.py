from __future__ import annotations

__all__: list[str] = []

import sys

import gravy.tests

sys.exit(1 - gravy.tests.test().wasSuccessful())
