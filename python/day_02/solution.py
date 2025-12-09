"""
--- Day 2: Gift Shop ---

You get inside and take the elevator to its only other stop: the gift shop.
"Thank you for visiting the North Pole!" gleefully exclaims a nearby sign.
You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database!
Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check.
For example:

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124

(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice.
So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

    11-22 has two invalid IDs, 11 and 22.
    95-115 has one invalid ID, 99.
    998-1012 has one invalid ID, 1010.
    1188511880-1188511890 has one invalid ID, 1188511885.
    222220-222224 has one invalid ID, 222222.
    1698522-1698528 contains no invalid IDs.
    446443-446449 has one invalid ID, 446446.
    38593856-38593862 has one invalid ID, 38593859.
    The rest of the ranges contain no invalid IDs.

Adding up all the invalid IDs in this example produces 1227775554.

What do you get if you add up all of the invalid IDs?

--- Part Two ---

The clerk quickly discovers that there are still invalid IDs in the ranges in your list.
Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

    11-22 still has two invalid IDs, 11 and 22.
    95-115 now has two invalid IDs, 99 and 111.
    998-1012 now has two invalid IDs, 999 and 1010.
    1188511880-1188511890 still has one invalid ID, 1188511885.
    222220-222224 still has one invalid ID, 222222.
    1698522-1698528 still contains no invalid IDs.
    446443-446449 still has one invalid ID, 446446.
    38593856-38593862 still has one invalid ID, 38593859.
    565653-565659 now has one invalid ID, 565656.
    824824821-824824827 now has one invalid ID, 824824824.
    2121212118-2121212124 now has one invalid ID, 2121212121.

Adding up all the invalid IDs in this example produces 4174379265.
What do you get if you add up all of the invalid IDs using these new rules?
"""

from __future__ import annotations

from pathlib import Path

DAY_DIR: Path = Path(__file__).parent
INPUTS: Path = DAY_DIR / "input.txt"
EXAMPLE: Path = DAY_DIR / "example.txt"

# ----- Common ----- #


def parse_ranges(input_text: str) -> list[tuple[int, int]]:
    """
    Parses the input text into a list of ranges. Each range is represented as a tuple
    of two integers (start, end).

    Parameters
    ----------
    input_text : str
        The input text containing the ranges in the format "start-end,start-end,...".

    Returns
    -------
    list[tuple[int, int]]
        A list of tuples representing the ranges, in the format
        [(start1, end1), (start2, end2), ...].
    """
    ranges = []
    for part in input_text.strip().split(","):
        start_str, end_str = part.split("-")
        ranges.append((int(start_str), int(end_str)))
    return ranges


# ----- Part 1 ----- #


def is_invalid_id_part1(num: int) -> bool:
    """
    Determines if a given number is an invalid product ID based on
    the criteria for part 1: it is invalide if it consists of a
    sequence of digits repeated twice. A leading zero disqualifies
    the number.

    Parameters
    ----------
    num : int
        The number to check.

    Returns
    -------
    bool
        Wether the number is an invalid product ID.
    """
    num_str = str(num)
    length = len(num_str)

    # Must have even length to be split in half
    if length % 2 != 0:
        return False

    # Split in half and check if both halves are equal
    half_length = length // 2
    first_half = num_str[:half_length]
    second_half = num_str[half_length:]

    # Check if they match and no leading zeros (except for "0" itself)
    if first_half == second_half and (first_half[0] != "0" or first_half == "0"):
        return True
    return False


def solve_part1(inputs: str) -> int:
    """
    Solves part 1 of the gift shop problem. We split the input into
    parsed ranges, then go through all numbers in each range and check
    if they are invalid product IDs. If they are, we add them to a
    running total.

    Parameters
    ----------
    inputs : str
        The input text containing the ranges.

    Returns
    -------
    int
        The sum of all invalid product IDs found in the ranges.
    """
    ranges = parse_ranges(inputs)
    invalid_id_sum = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id_part1(num):
                invalid_id_sum += num

    return invalid_id_sum


# ----- Part 2 ----- #


def is_invalid_id_part2(num: int) -> bool:
    """
    Determines if a given number is an invalid product ID based on
    the criteria for part 2: it is invalide if it consists of a
    sequence of digits repeated at least twice. A leading zero
    disqualifies the number.

    Parameters
    ----------
    num : int
        The number to check.

    Returns
    -------
    bool
        Wether the number is an invalid product ID.
    """
    num_str = str(num)
    length = len(num_str)

    # Check for all possible pattern lengths from 1 to
    # length//2 (we need at least 2 repetitions)
    for pattern_length in range(1, length // 2 + 1):
        # Check if the length is divisible by pattern length
        if length % pattern_length == 0:
            pattern: str = num_str[:pattern_length]

            # Check if no leading zeros (except for "0" itself)
            if pattern[0] == "0" and pattern != "0":
                continue

            # Check if the entire string is this pattern repeated
            num_repetitions = length // pattern_length
            if pattern * num_repetitions == num_str:
                return True

    return False


def solve_part2(inputs: str) -> int:
    """
    Solves part 1 of the gift shop problem. We split the input into
    parsed ranges, then go through all numbers in each range and check
    if they are invalid product IDs. If they are, we add them to a
    running total.

    Parameters
    ----------
    inputs : str
        The input text containing the ranges.

    Returns
    -------
    int
        The sum of all invalid product IDs found in the ranges.
    """
    ranges = parse_ranges(inputs)
    invalid_id_sum = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id_part2(num):
                invalid_id_sum += num

    return invalid_id_sum


# ----- Running ----- #

if __name__ == "__main__":
    inputs: str = INPUTS.read_text()

    # print(solve_part1(EXAMPLE.read_text()))
    solution1 = solve_part1(inputs)
    print(f"Part 1 answer: {solution1}")

    # print(solve_part2(EXAMPLE.read_text()))
    solution2 = solve_part2(inputs)
    print(f"Part 2 answer: {solution2}")
