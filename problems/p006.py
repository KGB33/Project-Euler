"""# Sum Square Difference
### Problem 6

The sum of the squares of the first ten natural
numbers is,

    12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural
numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the
squares of the first ten natural numbers and the
square of the sum is `3025 − 385 = 2640`.

Find the difference between the sum of the
squares of the first one hundred natural numbers and
the square of the sum.
"""
SOLUTION = 25164150


def test_correctness():
    assert SOLUTION == p006()


def p006():
    s = 0
    p = 0
    for i in range(101):
        s = s + i
        p = p + i * i
    s = s * s
    ssd = s - p
    return ssd


if __name__ == "__main__":
    from colorama import Fore

    answer = p006()
    if answer == SOLUTION:
        color = Fore.GREEN
    else:
        color = Fore.RED
    print(color + f"Solution to {__file__[-7:-3]}={answer}")
