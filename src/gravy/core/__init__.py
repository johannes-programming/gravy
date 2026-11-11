from __future__ import annotations

__all__: list[str] = ["calculate", "main", "parse_args", "run", "score"]


import argparse
import enum
import functools
import logging
import math
import tomllib
from collections.abc import Callable, Iterable
from importlib import metadata, resources
from typing import Any, Final, Self, cast


class Util(enum.Enum):
    """Utility for accessing configuration data."""

    util = None

    @functools.cached_property
    def data(self: Self) -> dict[str, Any]:
        """Return cached config data."""
        text: str
        text = resources.read_text("gravy.core", "cfg.toml")
        return tomllib.loads(text)


def main(args: Iterable[str] | None = None) -> int:
    """Calculate the GRAVY score of seq."""
    space: argparse.Namespace
    try:
        space = parse_args(args)
        run(**vars(space))
    except SystemExit as exit:
        if isinstance(exit.code, int):
            return int(exit.code)
        else:
            return int(bool(exit.code))
    except BaseException as exc:
        logging.exception(exc)
        return 1
    else:
        return 0


def parse_args(args: Iterable[str] | None = None) -> argparse.Namespace:
    parser: argparse.ArgumentParser
    version: str
    parser = argparse.ArgumentParser(
        add_help=False,
        description="This project calculates the GRAVY score.",
        fromfile_prefix_chars="@",
        prog="gravy",
    )
    parser.add_argument(
        "--format-spec", default=".5f", help="format of the output"
    )
    parser.add_argument("-h", "--help", action="help")
    version = "%(prog)s, version " + metadata.version("gravy")
    parser.add_argument("-V", "--version", action="version", version=version)
    parser.add_argument("seq")
    return parser.parse_args(args)


def run(seq: Iterable[object], *, format_spec: str = ".5f") -> None:
    """Print the formatted GRAVY score."""
    print(format(score(seq), format_spec))


def score(seq: Iterable[object]) -> float:
    """Calculate the GRAVY score."""
    item: object
    value: float
    values: list[float]

    values = []

    for item in seq:
        value = cast(float, Util.util.data["values"][str(item)])
        if not math.isnan(value):
            values.append(value)

    if values:
        return sum(values) / len(values)

    return float("nan")


calculate: Final[Callable[..., float]] = score
