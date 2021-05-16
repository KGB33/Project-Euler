"""
Longest Collatz sequence
Problem 14


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import math
import time
import operator

SOLUTION = 837799


class CollatzChain:
    def __init__(self):
        self.chains = {pow(2, n): n - 1 for n in range(0, 20)}

    def add_to_chains(self, num: int):
        terms = [
            num,
        ]
        while terms[-1] not in self.chains:
            if terms[-1] % 2 == 0:
                terms.append(doEven(terms[-1]))
            else:
                terms.append(doOdd(terms[-1]))
        chain_length = self.chains[terms[-1]]
        for i, val in enumerate(reversed(terms)):
            self.chains.update({val: i + chain_length})

    @property
    def largest_chain(self) -> int:
        return max(self.chains.items(), key=operator.itemgetter(1))[0]


def main() -> int:
    cc = CollatzChain()
    for num in range(5, 999999):
        cc.add_to_chains(num)
    return cc.largest_chain


def doEven(number):
    return number / 2


def doOdd(number):
    return 3 * number + 1


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
