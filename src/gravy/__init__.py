"""Calculate the GRAVY score of an amino acid sequence."""

__all__: list[str] = ["calculate", "main", "run", "score"]

import sys

from gravy.core import calculate, main, run, score

if __name__ == "__main__":
    sys.exit(main())
