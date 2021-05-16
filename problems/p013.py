"""
Large sum
Problem 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
 --->>> p13 - data <<<---
"""
import time
from pathlib import Path

SOLUTION = -1


def main():
    total = 0
    data = Path(__file__).parent.absolute() / "data" / "p013.txt"
    with open(data) as f:
        for line in f:
            total += int(line[:11])
    return str(total)[:10]


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
