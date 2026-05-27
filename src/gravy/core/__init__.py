__all__ = ["calculate", "main", "run", "score"]


import enum
import functools
import logging
import math
import tomllib
from collections.abc import Iterable
from importlib import resources
from typing import Any, Self, cast

import click
import preparse


class Util(enum.Enum):
    """Utility for accessing configuration data."""

    util = None

    @functools.cached_property
    def data(self: Self) -> dict[str, Any]:
        """Return cached config data."""
        text: str
        text = resources.read_text("gravy.core", "cfg.toml")
        return tomllib.loads(text)


def score(seq: Iterable[object]) -> float:
    """Calculate the GRAVY score."""
    values: list[float]
    item: object
    value: float

    values = []

    for item in seq:
        value = cast(float, Util.util.data["values"][str(item)])
        if not math.isnan(value):
            values.append(value)

    if values:
        return sum(values) / len(values)

    return float("nan")


calculate = score


@preparse.PreParser().click()
@click.command(add_help_option=False)
@click.option(
    "--format-spec",
    "f",
    help="format of the output",
    default=".5f",
    show_default=True,
)
@click.help_option("-h", "--help")
@click.version_option(None, "-V", "--version")
@click.argument("seq")
def main(seq: str, f: str) -> None:
    """Calculate the GRAVY score of seq."""
    try:
        run(seq, format_spec=f)
    except Exception:
        logging.exception("failed to calculate GRAVY score")


def run(seq: Iterable[object], *, format_spec: str = ".5f") -> None:
    """Print the formatted GRAVY score."""
    print(format(score(seq), format_spec))
