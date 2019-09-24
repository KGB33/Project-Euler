import time


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
    start_time = time.clock()
    print(p006())
    print(time.clock() - start_time)
