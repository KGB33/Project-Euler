#project Euler Problem 2, Even Fibonacci numbers
#success, answer was accepted
def count_fibonacci():
    e = 1
    e_hold = 1
    p = 1
    p_hold = 1
    sum_even = 0
    while e < 4000001:
        e_hold = e
        p_hold = p
        e = p + e
        p = e_hold
        if e%2==0:
            sum_even = sum_even + e
        print(e, sum_even)


count_fibonacci()
