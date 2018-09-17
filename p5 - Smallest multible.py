#project Euler, Problem 5

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

answer = 232792560
"""

def main():
    numbers = [12,13,14,15,16,17,18,19,20]
    winner = 11
    for element in numbers:
        winner = lcm(winner, element)
        print(winner)
    
     

def lcm(a,b):
    return a * b // gcd(a, b)
      
    
def gcd(a,b):
    while b:      
        a, b = b, a % b
    return a

main()