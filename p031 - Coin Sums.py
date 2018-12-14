# Coin sums
# Problem 31
"""
In England the currency is made up of
    pound, £, and
    pence, p,

There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
from PrimeTools import timer


@timer(unit='s')
def p031():
    total = 0
    for a in range(0, 200 + 1):
        for b in range(0, coin_range(2, a)):
            for c in range(0, coin_range(5, a, b)):
                for d in range(0, coin_range(10, a, b, c)):
                    for e in range(0, coin_range(20, a, b, c, d)):
                        for f in range(0, coin_range(50, a, b, c, d, e)):
                            for g in range(0, coin_range(100, a, b, c, d, e, f)):
                                for h in range(0, coin_range(200, a, b, c, d, e, f, g)):
                                    change = sum_pence([a, b, c, d, e, f, g, h])
                                    if change == 200:
                                        total += 1
                                        break
                                    elif change > 200:
                                        break
                                    else:
                                        continue
    print('\nSolution: {}'.format(total))


def sum_pence(*coins):
    total = 0
    value = [1, 2, 5, 10, 20, 50, 100, 200]
    for c, v in zip(*coins, value):
        total += c * v
    return total


def coin_range(value, *previous_coins):
    return ((200 - sum_pence(previous_coins)) // value) + 1


#print(sum_pence(1, 2))
p031()



# Notes

"""
To make it easier to type, £ = #

We have 1# = 100p

There are 8 increments of coins:

      1p        (a)
      2p        (b)
      5p        (c)
     10p        (d)
     20p        (e)
     50p        (f)
    100p (1#)   (g)
    200p (2#)   (h)
"""
