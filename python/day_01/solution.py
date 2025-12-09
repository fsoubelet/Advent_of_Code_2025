"""
--- Day 1: Secret Entrance ---

The Elves have good news and bad news.

The good news is that they've discovered project management!
This has given them the tools they need to prevent their usual Christmas emergency.
For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.

The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole!

To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

Collect stars by solving puzzles.
Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first.
Each puzzle grants one star. Good luck!

You arrive at the secret entrance to the North Pole base ready to start decorating.
Unfortunately, the password seems to have been changed, so you can't get in.
A document taped to the wall helpfully explains:

"Due to new security protocols, the password is locked in the safe below.
Please see the attached document for the new combination."

The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order.
As you turn the dial, it makes a small click noise as it reaches each number.

The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe.
A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers).
Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19.
After that, a rotation of L19 would cause it to point at 0.

Because the dial is a circle, turning the dial left from 0 one click makes it point at 99.
Similarly, turning the dial right from 99 one click makes it point at 0.

So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95.
After that, a rotation of R5 could cause it to point at 0.

The dial starts by pointing at 50.

You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy.
The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

For example, suppose the attached document contained the following rotations:

L68
L30
R48
L5
R60
L55
L1
L99
R14
L82

Following these rotations would cause the dial to move as follows:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32.

Because the dial points at 0 a total of three times during this process, the password in this example is 3.

Analyze the rotations in your attached document.
What's the actual password to open the door?

--- Part Two ---

You're sure that's the right password, but the door won't open. You knock, but nobody answers.
You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation.
So, in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door?
"""

from __future__ import annotations

from pathlib import Path

DAY_DIR = Path(__file__).parent

# ----- Part 1 ----- #


def turn_dial_part1(current_value: int, rotation: str) -> int:
    """
    Takes in the rotation (one line instruction from the input) as well
    as the current value of the dial, and returns the new value of the
    dial after the rotation.

    Note
    ----
    Is it taken into account that the dial is circular with values from
    0 to 99, inclusive. This means that turning left from 0 goes to 99,
    and turning right from 99 goes to 0. This is handled using modulo.

    Parameters
    ----------
    current_value : int
        The current value of the dial.
    rotation : str
        The rotation instruction (e.g., "L68", "R30").

    Returns
    -------
    int
        The new value of the dial after the rotation.
    """
    # The rotation is a letter (L or R) followed by a number
    direction = rotation[0]
    distance = int(rotation[1:])

    # Execute the rotation: determine the result via the correct
    # operation and modulo
    if direction == "L":
        new_value = (current_value - distance) % 100
    else:  # it's R, trust aoc inputs
        new_value = (current_value + distance) % 100

    return new_value


def solve_part1(starting_value: int, full_inputs: list[str]) -> int:
    """
    Solves part 1 of the puzzle. We take inputs one by one and turn
    the dial accordingly, counting how many times we end up on 0.

    Parameters
    ----------
    full_inputs : list[str]
        The list of rotation instructions.

    Returns
    -------
    int
        The number of times the dial points at 0.
    """
    dial_value = starting_value
    zero_counter = 0

    # Execute the rotations one by one
    for rotation in full_inputs:
        dial_value = turn_dial_part1(dial_value, rotation)
        if dial_value == 0:
            zero_counter += 1
    return zero_counter


# ----- Part 2 ----- #


def solve_part2(starting_value: int, full_inputs: list[str]) -> int:
    """
    Solves part 2 of the puzzle. We take inputs one by one and turn
    the dial accordingly, counting how many times we pass through 0
    during the rotations, as well as how many times we end up on 0.

    Note
    ----
    It is important to note that ending on the value 0 does not count
    as passing through 0 during the rotation! Similarly, starting on 0
    and rotating away from it does not count as passing through 0! This
    is handled by a more brute force solution of doing every single click
    and checking if we **end up** on 0 after each click.

    Parameters
    ----------
    full_inputs : list[str]
        The list of rotation instructions.

    Returns
    -------
    int
        The number of times the dial points at 0 or passes through 0.
    """
    dial_value: int = starting_value
    zero_counter: int = 0

    # Execute the rotations one by one
    for rotation in full_inputs:
        # The rotation is a letter (L or R) followed by a number
        direction: str = rotation[0]
        clicks: int = int(rotation[1:])

        # Execute the rotation: we do each click one by one and check
        # after each if we end up on 0 (that's a pass if not the last)
        # click, and ending on a 0 if the last click).
        for _ in range(clicks):
            if direction == "L":
                dial_value = (dial_value - 1) % 100
            else:  # it's R, trust aoc inputs
                dial_value = (dial_value + 1) % 100

            # Now we check if we're on a 0
            if dial_value == 0:
                zero_counter += 1

    return zero_counter


# ----- Running ----- #

if __name__ == "__main__":
    inputs = (DAY_DIR / "input.txt").read_text().splitlines()

    starting_value = 50  # given by the puzzle description
    solution1 = solve_part1(starting_value, inputs)
    print(f"Part 1 answer: {solution1}")

    solution2 = solve_part2(starting_value, inputs)
    print(f"Part 2 answer: {solution2}")
