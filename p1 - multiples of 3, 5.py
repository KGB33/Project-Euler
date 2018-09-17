#Project Euler, Problem One, Multiples of 3 and 5
#success, answer was accepted
import math
import numbers
def find_multiples():
    n = 0
    grand_sum = 0
    while n < 1000:
        if n%3==0:
            grand_sum = grand_sum + n
            print(grand_sum, n)
            n = n+1
        elif n%5==0:
            grand_sum = grand_sum + n
            print(grand_sum, n)
            n = n+1
        else:
            print(grand_sum, n)
            n = n+1


find_multiples()

