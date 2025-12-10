"""

"""

from __future__ import annotations

from pathlib import Path

DAY_DIR: Path = Path(__file__).parent
INPUTS: Path = DAY_DIR / "input.txt"
EXAMPLE: Path = DAY_DIR / "example.txt"

# ----- Common ----- #



# ----- Part 1 ----- #





def solve_part1(inputs: str) -> int:
    """
    Solves part 1
    """
    return 0


# ----- Part 2 ----- #





def solve_part2(inputs: str) -> int:
    """
    Solves part 2
    """
    return 0


# ----- Running ----- #

if __name__ == "__main__":
    inputs: str = INPUTS.read_text()

    print(solve_part1(EXAMPLE.read_text()))
    # solution1 = solve_part1(inputs)
    # print(f"Part 1 answer: {solution1}")

    # print(solve_part2(EXAMPLE.read_text()))
    # solution2 = solve_part2(inputs)
    # print(f"Part 2 answer: {solution2}")
