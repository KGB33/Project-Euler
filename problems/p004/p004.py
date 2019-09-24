import time


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
    start_time = time.clock()
    print(p004())
    print(time.clock() - start_time)
