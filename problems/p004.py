"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two
2-digit numbers is `9009 = 91 × 99`.

Find the largest palindrome made from the product
of two 3-digit numbers.
"""

SOLUTION = 906609


def test_correctness():
    assert SOLUTION == p004()


def p004():
    winner = 0
    for n in range(999, 100, -1):
        for m in range(999, 100, -1):
            number = str(n * m)
            if number == number[::-1]:
                if int(number) > winner:
                    winner = int(number)
                    break

    return winner


if __name__ == "__main__":
    from colorama import Fore

    answer = p004()
    if answer == SOLUTION:
        color = Fore.GREEN
    else:
        color = Fore.RED
    print(color + f"Solution to {__file__[-7:-3]}={answer}")
