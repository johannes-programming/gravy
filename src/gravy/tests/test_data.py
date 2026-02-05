import enum
import functools
import math
import tomllib
import unittest
from importlib import resources
from typing import *

from gravy.core import score

__all__ = ["TestScoreFunction"]


class Util(enum.Enum):
    util = None

    @functools.cached_property
    def data(self: Self) -> dict:
        "This cached property holds the cfg data."
        text: str
        text = resources.read_text("gravy.tests", "testdata.toml")
        return tomllib.loads(text)


class TestScoreFunction(unittest.TestCase):
    def go(self: Self, x: str, y: str, /) -> None:
        z: float
        z = score(x)
        if math.isnan(y):
            self.assertTrue(math.isnan(z))
        else:
            self.assertEqual(y, z)

    def test_scores(self: Self) -> None:
        x: str
        y: float
        for x, y in Util.util.data["scores"].items():
            self.go(x, y)


if __name__ == "__main__":
    unittest.main()
