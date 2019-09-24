from PrimeTools import prime_factors


def p003():
    number = 600851475143
    return max(prime_factors(number).keys())


if __name__ == "__main__":
    print(p003())
