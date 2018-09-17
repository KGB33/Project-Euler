#Project Euler, Problem 3, Largest Prime Factor
#success

def prime_factor():
    number = int(input('What number do you want to Prime Facotr? '))
    n = 2
    factors = (1,)
    while n <= number:
        if number%n==0:
            factors = factors + (n,)
            print(n, factors, len(factors))
            number = number/n
        else:
            n=n+1
    prime_factor()


prime_factor()
