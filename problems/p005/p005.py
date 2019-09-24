import time


def p005():
    numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20]
    winner = 11
    for element in numbers:
        winner = lcm(winner, element)
    return winner


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    start_time = time.clock()
    print(p005())
    print(time.clock() - start_time)
