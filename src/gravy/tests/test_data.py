import enum
import functools
import math
import tomllib
import unittest
from collections.abc import Iterator
from importlib import resources
from typing import Any, Self

from gravy.core import score

__all__ = ["TestScoreFunction"]


class Util(enum.Enum):
    """Utility for test data."""

    util = None

    @functools.cached_property
    def data(self: Self) -> dict[str, Any]:
        """Return cached test data."""
        text: str
        text = resources.read_text("gravy.tests", "testdata.toml")
        return tomllib.loads(text)


class TestScoreFunction(unittest.TestCase):
    """Tests for the score function using test data."""

    def go(self: Self, x: Any, y: Any, /) -> None:
        """Helper to test a single score."""
        z: float
        z = score(x)
        if math.isnan(y):
            self.assertTrue(math.isnan(z))
        else:
            self.assertEqual(y, z)

    def test_scores(self: Self) -> None:
        """Test scores from testdata."""
        x: str
        y: float
        for x, y in Util.util.data["scores"].items():
            self.go(x, y)


if __name__ == "__main__":
    unittest.main()
