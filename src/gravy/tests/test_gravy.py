import unittest
from typing import *

from gravy.core import score

__all__ = ["TestScoreFunction"]


class TestScoreFunction(unittest.TestCase):

    def test_valid_sequence(self: Self) -> None:
        "Test a valid sequence with known values."
        expected_score: float
        seq: str
        seq = "ACDEFGHIKLMNPQRSTVWY"
        expected_score = (
            1.8
            + 2.5
            - 3.5
            - 3.5
            + 2.8
            - 0.4
            - 3.2
            + 4.5
            - 3.9
            + 3.8
            + 1.9
            - 3.5
            - 1.6
            - 3.5
            - 4.5
            - 0.8
            - 0.7
            + 4.2
            - 0.9
            - 1.3
        ) / 20
        self.assertAlmostEqual(score(seq), expected_score)

    def test_sequence_with_gap(self: Self) -> None:
        "Test a sequence with gaps ('-')."
        expected_score: float
        seq: str
        seq = "ACDEFGHI-KLMNPQRSTVWY"
        expected_score = (
            1.8
            + 2.5
            - 3.5
            - 3.5
            + 2.8
            - 0.4
            - 3.2
            + 4.5
            - 3.9
            + 3.8
            + 1.9
            - 3.5
            - 1.6
            - 3.5
            - 4.5
            - 0.8
            - 0.7
            + 4.2
            - 0.9
            - 1.3
        ) / 20
        self.assertAlmostEqual(score(seq), expected_score)

    def test_sequence_with_unknown_values(self: Self) -> None:
        "Test a sequence with unknown or unsupported values ('X')."
        expected_score: float
        seq: str
        seq = "ACDEXFGHIKLMNPQRSTVWY"
        expected_score = (
            1.8
            + 2.5
            - 3.5
            - 3.5
            + 2.8
            - 0.4
            - 3.2
            + 4.5
            - 3.9
            + 3.8
            + 1.9
            - 3.5
            - 1.6
            - 3.5
            - 4.5
            - 0.8
            - 0.7
            + 4.2
            - 0.9
            - 1.3
        ) / 20
        self.assertAlmostEqual(score(seq), expected_score)


if __name__ == "__main__":
    unittest.main()
