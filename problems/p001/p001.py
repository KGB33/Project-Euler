def find_multiples():
    grand_sum = 0
    for n in range(1000):
        if n % 3 == 0:
            grand_sum += n
        elif n % 5 == 0:
            grand_sum += n
    return grand_sum


def array_way():
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


if __name__ == "__main__":
    print(array_way())
    print(find_multiples())
