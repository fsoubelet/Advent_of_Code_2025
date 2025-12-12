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
    Solves part 1. Determines from the complete input
    how many rolls of paper can be accessed by a forklift.
    This is done by going over each position in the grid
    and checking for the eight adjacent positions while
    coubting the number of rolls of paper (@) found.

    Note
    ----
    We denote i the index along the vertical axis (rows)
    and j the index along the horizontal axis (columns).
    Inspecting for a position at indices (i, j) requires
    checking the following relative positions:
        - (i-1, j-1) : top left
        - (i-1, j)   : top
        - (i-1, j+1) : top right
        - (i, j-1)   : left
        - (i, j+1)   : right
        - (i+1, j-1) : bottom left
        - (i+1, j)   : bottom
        - (i+1, j+1) : bottom right

    If any of these positions are out of bounds, then they
    are simply ignored. Naturally, a position is not checked
    if it does not contain a roll of paper (@).

    Parameters
    ----------
    inputs : list[str]
        The input lines representing banks of batteries.

    Returns
    -------
    int
        The number of rolls of paper that can be accessed
        by a forklift.
    """
    reachable_rolls: int = 0

    n_rows: int = len(inputs)
    n_cols: int = len(inputs[0])

    # We need to be careful that Python list indexing does
    # a looparound when using negative indices.
    for i in range(n_rows):
        for j in range(n_cols):
            # Move on if position (i, j) is not a paper roll
            if inputs[i][j] != "@":
                continue

            # Count the number of adjacent paper rolls
            adjacent_rolls: int = 0
            for i_inc in [-1, 0, 1]:
                for j_inc in [-1, 0, 1]:
                    # Skip the position itself
                    if i_inc == 0 and j_inc == 0:
                        continue

                    ni: int = i + i_inc
                    nj: int = j + j_inc

                    # Check for out of bounds
                    if ni < 0 or ni >= n_rows:
                        continue
                    if nj < 0 or nj >= n_cols:
                        continue

                    # Count adjacent paper roll
                    if inputs[ni][nj] == "@":
                        adjacent_rolls += 1

            # Check if the roll is reachable
            if adjacent_rolls < 4:
                reachable_rolls += 1
                # print(i, j)  # so we can check on the example

    return reachable_rolls


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
    solution1 = solve_part1(inputs)
    print(f"Part 1 answer: {solution1}")

    # print(solve_part2(EXAMPLE.read_text().splitlines()))
    # solution2 = solve_part2(inputs)
    # print(f"Part 2 answer: {solution2}")
