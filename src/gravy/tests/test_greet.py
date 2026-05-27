"""Tests for the run function."""

__all__ = ["TestGreet"]
import unittest
from contextlib import redirect_stdout
from io import StringIO
from typing import Self

from gravy.core import run


class TestGreet(unittest.TestCase):
    """Test greet functionality via run."""

    def test_output(self: Self) -> None:
        """Test output of run function."""
        captured: StringIO
        captured = StringIO()
        with redirect_stdout(captured):
            run("SPAM", format_spec=".2f")
        self.assertEqual(captured.getvalue(), "0.32\n")


if __name__ == "__main__":
    unittest.main()
