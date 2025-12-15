"""
--- Day 4: Printing Department ---

"""

from __future__ import annotations

from pathlib import Path
from pprint import pprint  # noqa: F401

DAY_DIR: Path = Path(__file__).parent
INPUTS: Path = DAY_DIR / "input.txt"
EXAMPLE: Path = DAY_DIR / "example.txt"


# ----- Part 1 ----- #


def solve_part1(inputs: list[str]) -> int:
    """
    Solves part 1.

    Parameters
    ----------
    inputs : list[str]
        The input lines representing banks of batteries.

    Returns
    -------
    int
    """
    return 0


# ----- Part 2 ----- #

def solve_part2(inputs: list[str]) -> int:
    """
    Solves part 2.
    Parameters
    ----------
    inputs : list[str]
        The input lines representing banks of batteries.

    Returns
    -------
    int
    """
    return 0


# ----- Running ----- #

if __name__ == "__main__":
    inputs: list[str] = INPUTS.read_text().splitlines()

    # print(solve_part1(EXAMPLE.read_text().splitlines()))
    # solution1 = solve_part1(inputs)
    # print(f"Part 1 answer: {solution1}")

    # print(solve_part2(EXAMPLE.read_text().splitlines()))
    # solution2 = solve_part2(inputs)
    # print(f"Part 2 answer: {solution2}")
