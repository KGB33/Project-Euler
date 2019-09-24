import time
from PrimeTools import division_test


def p007():
    i = 2
    p = 3
    while i != 10001:
        p += 2
        if division_test(p):
            i += 1
    return p


if __name__ == "__main__":
    start_time = time.clock()
    print(p007())
    print(time.clock() - start_time)
