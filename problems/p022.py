"""
Names scores
Problem 22
Using 'p022 - data.txt' a 46K text file containing over five-thousand first names,

> begin by sorting it into alphabetical order.
> Then working out the alphabetical value for each name
        multiply this value by its alphabetical position in the list to obtain a name score.


For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import time

SOLUTION = 871198282


def main():
    total = 0
    with open("data/p022.txt") as names:
        data = names.read().split(",")
        data.sort()
    for i in range(0, len(data)):
        total += get_alphabetical_value(data[i]) * (i + 1)
    return total


def get_alphabetical_value(string):
    get_val = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
        '"': 0,
    }
    total = 0
    for letter in string:
        total += get_val[letter]
    return total


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
