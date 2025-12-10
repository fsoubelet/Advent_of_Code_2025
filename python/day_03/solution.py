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

--- Part Two ---

The escalator doesn't move.
The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button.
You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

Consider again the example from before:

987654321111111
811111111111119
234234234234278
818181911112111

Now, the joltages are much larger:

    In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

What is the new total output joltage?
"""

from __future__ import annotations

from pathlib import Path

DAY_DIR: Path = Path(__file__).parent
INPUTS: Path = DAY_DIR / "input.txt"
EXAMPLE: Path = DAY_DIR / "example.txt"


# ----- Part 1 ----- #


def find_bank_joltage_part1(bank: str) -> int:
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
        total_joltage += find_bank_joltage_part1(bank)

    return total_joltage


# ----- Part 2 ----- #


def find_bank_joltage_part2(bank: str) -> int:
    """
    Provided with a bank of batteries as a string, finds the maximum
    joltage possiblly attainable by turning on TWELVE batteries. This is
    done by going through all possible combinations of 12 batteries (still
    preserving left-right order) and checking which produces the largest
    number.

    Note
    ----
    There is probably a more elegant way to do this, but considering that
    12 is not that large, brute writing out the various loops is doable
    and has the advantage of being explicit and clear.

    Parameters
    ----------
    bank : str
        A string digits representing a bank of batteries.

    Returns
    -------
    int
        The maximum joltage possible by turning on twelve batteries.
    """
    max_joltage: int = 0

    # We go through all the possible combinations of 12 batteries
    for i1 in range(len(bank)):
        for i2 in range(i1 + 1, len(bank)):
            for i3 in range(i2 + 1, len(bank)):
                for i4 in range(i3 + 1, len(bank)):
                    for i5 in range(i4 + 1, len(bank)):
                        for i6 in range(i5 + 1, len(bank)):
                            for i7 in range(i6 + 1, len(bank)):
                                for i8 in range(i7 + 1, len(bank)):
                                    for i9 in range(i8 + 1, len(bank)):
                                        for i10 in range(i9 + 1, len(bank)):
                                            for i11 in range(i10 + 1, len(bank)):
                                                for i12 in range(i11 + 1, len(bank)):
                                                    # Form the joltage by turning on batteries at these positions
                                                    joltage: int = int(
                                                        bank[i1]
                                                        + bank[i2]
                                                        + bank[i3]
                                                        + bank[i4]
                                                        + bank[i5]
                                                        + bank[i6]
                                                        + bank[i7]
                                                        + bank[i8]
                                                        + bank[i9]
                                                        + bank[i10]
                                                        + bank[i11]
                                                        + bank[i12]
                                                    )
                                                    # Check if this is the largest we've seen so far
                                                    if joltage > max_joltage:
                                                        max_joltage = joltage
    return max_joltage


def solve_part2(inputs: list[str]) -> int:
    """
    Solves part 2 We go find the maximum joltage for each bank (input
    line) with the new rules of part 2 and sum all of these up.

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
        print(bank)
        total_joltage += find_bank_joltage_part2(bank)

    return total_joltage


# ----- Running ----- #

if __name__ == "__main__":
    inputs: list[str] = INPUTS.read_text().splitlines()

    # print(solve_part1(EXAMPLE.read_text().splitlines()))
    solution1 = solve_part1(inputs)
    print(f"Part 1 answer: {solution1}")

    # print(solve_part2(EXAMPLE.read_text().splitlines()))
    solution2 = solve_part2(inputs)
    print(f"Part 2 answer: {solution2}")
