"""
--- Day 4: Printing Department ---

You ride the escalator down to the printing department.
They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations.
What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help.
"We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving.
It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions.
If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Consider your complete diagram of the paper roll locations.
How many rolls of paper can be accessed by a forklift?
"""

from __future__ import annotations

from pathlib import Path

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

    print(solve_part1(EXAMPLE.read_text().splitlines()))
    # solution1 = solve_part1(inputs)
    # print(f"Part 1 answer: {solution1}")

    # print(solve_part2(EXAMPLE.read_text().splitlines()))
    # solution2 = solve_part2(inputs)
    # print(f"Part 2 answer: {solution2}")
