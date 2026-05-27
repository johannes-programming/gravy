"""Entry point for running all tests."""

import unittest
from collections.abc import Iterator
from typing import Self

__all__ = ["test"]


def test() -> unittest.TextTestResult:
    """Run all the tests."""
    loader: unittest.TestLoader
    tests: unittest.TestSuite
    runner: unittest.TextTestRunner
    result: unittest.TextTestResult
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir="gravy.tests")
    runner = unittest.TextTestRunner()
    result = runner.run(tests)
    return result
