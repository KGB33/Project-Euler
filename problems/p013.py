"""
Large sum
Problem 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
 --->>> p13 - data <<<---
"""
SOLUTION = -1

from pathlib import Path


def p013():
    total = 0
    data = Path(__file__).parent.absolute() / "data" / "p013_data.txt"
    with open(data) as f:
        for line in f:
            total += int(line[:11])
    return str(total)[:10]


def test_p013():
    assert SOLUTION == p013()


if __name__ == "__main__":
    from colorama import Fore

    answer = p013()
    if answer == SOLUTION:
        color = Fore.GREEN
    else:
        color = Fore.RED
    print(color + f"Solution to {__file__[-7:-3]}={answer}")
