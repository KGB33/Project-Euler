# Digit fifth powers
#     Problem 30
"""
    Surprisingly there are only three numbers that can be
written as the sum of fourth powers of their digits:

        1634 = 1^4 + 6^4 + 3^4 + 4^4
        8208 = 8^4 + 2^4 + 0^4 + 8^4
        9474 = 9^4 + 4^4 + 7^4 + 4^4

            As 1 = 1^4
        is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
from PrimeTools import timer


@timer(unit="s")
def p030():
    numbers_found = []
    for number in range(2, 1000000):
        s_num = str(number)
        total = 0
        for digit in s_num:
            total += pow(int(digit), 5)
        if total == number:
            numbers_found.append(number)
    print("Solution: {}" "\n\tNumbers: {}".format(sum(numbers_found), numbers_found))


p030()

# Notes:

# Definitions:
"""
        DFP = Digit 5th Powers
"""

# Establishing an upper-bound:
"""
        There is a point where the DFP of a number MUST be less than the number,
        for example:
        
            DFP(999...999) < 999...999
            
        We can determine how many digits's are necessary by trial and error:
        
            Start with a 10 digit number where every digit is a 9.
                
                10 * 9 ^ 5 = 590,490 < 9,999,999,999
            
            5 digit:
                
                5 * 9 ^ 5 = 295,245 > 99,999
                
            7 digit:
            
                7 * 9 ^ 5 = 413,343 < 9,999,999
                
            6 digit: 6 * 9 ^ 5 = 354,294 < 999,999
            
        Therefore, our largest number is between 5 - 6 digits,
        hence the upper-bound is 1,000,000
"""
