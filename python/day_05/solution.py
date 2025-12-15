"""
--- Day 5: Cafeteria ---

As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen.
"At this rate, we won't have any time left to put the wreaths up in the dining hall!".
Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims.
You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled.
When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs.
It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs.
For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32

The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh.
The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh.
In this example, this is done as follows:

    Ingredient ID 1 is spoiled because it does not fall into any range.
    Ingredient ID 5 is fresh because it falls into range 3-5.
    Ingredient ID 8 is spoiled.
    Ingredient ID 11 is fresh because it falls into range 10-14.
    Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
    Ingredient ID 32 is spoiled.

So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system.
How many of the available ingredient IDs are fresh?

--- Part Two ---

The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh.
An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant.
Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18

The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20.
So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again.
How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
"""

from __future__ import annotations

from pathlib import Path

DAY_DIR: Path = Path(__file__).parent
INPUTS: Path = DAY_DIR / "input.txt"
EXAMPLE: Path = DAY_DIR / "example.txt"


# ----- Common ----- #


def get_ranges_and_ids(inputs: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    """
    Parses the input lines into the ranges of fresh ingredients as
    well as the available ingredient IDs.

    The distinction between these two sections is a blank line in
    the input, which would be an empty list after we've split the
    input into lines.

    Parameters
    ----------
    inputs : list[str]
        The input lines.
    """
    # Trust the input in aoc, there's only one blank line
    blank_line_idx: int = inputs.index("")
    ranges_lines: list[str] = inputs[:blank_line_idx]
    ids_lines: list[str] = inputs[blank_line_idx + 1 :]

    # Cast to the actual expected types
    ranges: list[tuple[int, int]] = [
        (int(line.split("-")[0]), int(line.split("-")[-1])) for line in ranges_lines
    ]
    ids: list[int] = [int(line) for line in ids_lines]
    return ranges, ids


# ----- Part 1 ----- #


def solve_part1(inputs: list[str]) -> int:
    """
    Solves part 1. We parse the inputs into the ranges of fresh
    ingredient IDs and the available ingredient IDs, then count
    how many of the available IDs fall into any of the fresh ranges.

    This is done by brute force, by looping over the available IDs
    and checking against the ranges. We can stop checking the ranges
    as soon as one contains the ID.

    Parameters
    ----------
    inputs : list[str]
        The input lines representing the ranges and IDs.

    Returns
    -------
    int
        The number of available ingredients that are fresh.
    """
    number_of_fresh_ingredients: int = 0
    fresh_ranges, available_ids = get_ranges_and_ids(inputs)

    # We go and check for each available ID
    for id in available_ids:
        # We check against all ranges to check if it falls in
        for range_start, range_end in fresh_ranges:
            if range_start <= id <= range_end:
                # print(f"ID {id} is fresh: in range ({range_start}-{range_end})")  # so we can check on the example
                number_of_fresh_ingredients += 1
                break  # No need to check further ranges

    # Return the total count
    return number_of_fresh_ingredients


# ----- Part 2 ----- #


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Merge overlapping ranges into single ranges, for easier
    counting of unique IDs later on. For instance, the ranges
    (3-5) and (5-8) would be merged into (3-8).

    Note
    ----
    This is done sorting the ranges and then going over them,
    removing any start or end if it falls into the previous range.

    Parameters
    ----------
    ranges : list[tuple[int, int]]
        The list of ranges to merge.

    Returns
    -------
    list[tuple[int, int]]
        The merged ranges.
    """
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    # Go over the ranges and merge as needed
    for start, end in sorted_ranges[1:]:  # we already took the first range
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # this range starts in the previous one
            merged[-1] = (last_start, max(last_end, end))  # extend the previous range
        else:
            merged.append((start, end))  # no overlap, just add

    return merged


def solve_part2(inputs: list[str]) -> int:
    """
    Solves part 2. We parse the inputs into the ranges of fresh
    ingredient IDs and the available ingredient IDs, the latter
    is discarded for this part.

    We start by sorting then merging ranges so that they are ordered
    and unique: no ID sits in multiple ranges. The final result is
    a matter of accumulating the lengths of each range.

    Parameters
    ----------
    inputs : list[str]
        The input lines representing the ranges and IDs.

    Returns
    -------
    int
        The number of ingredient IDs that are considered fresh
        according to the fresh ranges.
    """
    fresh_ranges, _ = get_ranges_and_ids(inputs)
    merged_ranges = merge_ranges(fresh_ranges)
    number_of_valid_ids: int = 0

    # We go over each range and count the number of IDs in it
    for range_start, range_end in merged_ranges:
        # print(f"Range ({range_start}-{range_end}) with length {range_end - range_start + 1}")

        # Since the ranges have been ordered and merged, we can be sure
        # there is no element in multiple ranges. We can then just add
        # the length of the range to the total count (number of IDs in it)
        number_of_valid_ids += range_end - range_start + 1

    # We return the number of unique valid IDs
    return number_of_valid_ids


# ----- Running ----- #

if __name__ == "__main__":
    inputs: list[str] = INPUTS.read_text().splitlines()

    # print(solve_part1(EXAMPLE.read_text().splitlines()))
    # solution1 = solve_part1(inputs)
    # print(f"Part 1 answer: {solution1}")

    # print(solve_part2(EXAMPLE.read_text().splitlines()))
    solution2 = solve_part2(inputs)
    print(f"Part 2 answer: {solution2}")
