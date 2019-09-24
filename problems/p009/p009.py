def p009():
    a = 1
    b = 1
    while True:
        c = 1000 - a - b
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            print(f"a: {a}, b: {b}, c: {c}")
            return a * b * c
        else:
            if a > 1000:
                a = 1
                b += 1
            else:
                a += 1


if __name__ == "__main__":
    print(p009())
