"""
--- Day 3: Lobby ---

You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint.
When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel.
"Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

You explain your need to get further underground.
"Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working.
That is, you could if the escalator weren't also offline."

"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

There are batteries nearby that can supply emergency power to the escalator for just such an occasion.
The batteries are each labeled with their joltage rating, a value from 1 to 9.
You make a note of their joltage ratings (your puzzle input). For example:

987654321111111
811111111111119
234234234234278
818181911112111

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries.
Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on.
For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce. In the above example:

    In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    In 818181911112111, the largest joltage you can produce is 92.

The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

There are many batteries in front of you.
Find the maximum joltage possible from each bank; what is the total output joltage?
"""

from __future__ import annotations

from pathlib import Path

DAY_DIR: Path = Path(__file__).parent
INPUTS: Path = DAY_DIR / "input.txt"
EXAMPLE: Path = DAY_DIR / "example.txt"

# ----- Common ----- #


def find_bank_joltage(bank: str) -> int:
    """
    Provided with a bank of batteries as a string, finds the maximum
    joltage possiblly attainable by turning on two batteries. This is
    done by going through all possible combinations of 2 batteries (still
    preserving left-right order) and checking which produces the largest
    number.

    Note
    ----
    It is not possible to just look for the two highest digits since the
    order of the digits matters. For instance, in the fourth example line,
    the two highest digits are 8 and 9. Due to the order they assemble to
    89. However there is the possibility to assemble 9 and a later 2 for
    a joltage of 92.

    Parameters
    ----------
    bank : str
        A string digits representing a bank of batteries.

    Returns
    -------
    int
        The maximum joltage possible by turning on two batteries.
    """
    max_joltage: int = 0

    # We go through all the possible pairs of batteries
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form the joltage by turning on batteries at position i and j
            joltage: int = int(bank[i] + bank[j])

            # Check if this is the largest we've seen so far
            if joltage > max_joltage:
                max_joltage = joltage

    return max_joltage


# ----- Part 1 ----- #


def solve_part1(inputs: list[str]) -> int:
    """
    Solves part 1. We go find the maximum joltage for each bank (input
    line) and sum all of these up.

    Parameters
    ----------
    inputs : list[str]
        The input lines representing banks of batteries.

    Returns
    -------
    int
        The total output joltage.
    """
    total_joltage: int = 0

    for bank in inputs:
        total_joltage += find_bank_joltage(bank)

    return total_joltage


# ----- Part 2 ----- #


def solve_part2(inputs: list[str]) -> int:
    """
    Solves part 2
    """
    return 0


# ----- Running ----- #

if __name__ == "__main__":
    inputs: list[str] = INPUTS.read_text().splitlines()

    # print(solve_part1(EXAMPLE.read_text().splitlines()))
    solution1 = solve_part1(inputs)
    print(f"Part 1 answer: {solution1}")

    # print(solve_part2(EEXAMPLE.read_text().splitlines()))
    # solution2 = solve_part2(inputs)
    # print(f"Part 2 answer: {solution2}")
