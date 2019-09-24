import time


def count_fibonacci():
    e = 1
    p = 1
    sum_even = 0
    while e < 4000001:
        e_hold = e
        e = p + e
        p = e_hold
        if e % 2 == 0:
            sum_even += e
    return sum_even


if __name__ == "__main__":
    start_time = time.clock()
    print(count_fibonacci())
    print(time.clock() - start_time)
