"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE:
Do not count spaces or hyphens.
For example:

-> 342 (three hundred and forty-two) contains 23 letters
-> 115 (one hundred and fifteen) contains 20 letters.

The use of "and" when writing out numbers is in compliance with British usage.
"""
import time
import inflect  # is using this cheating, maybe, maybe not, who knows

SOLUTION = 21124


def main():
    total_letters = 0
    ie = inflect.engine()
    for _ in range(1, 1000 + 1):
        word = ie.number_to_words(_)
        for letter in word:
            if letter == "-":
                pass
            elif letter == " ":
                pass
            else:
                total_letters += 1

    return total_letters


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
