"""# Special Pythagorean Triplet
### Problem 9

A Pythagorean triplet is a set of three natural numbers,
`a < b < c`, for which,

`a² + b² = c²`
For example, `3² + 4² = 9 + 16 = 25 = 5²`.

There exists exactly one Pythagorean triplet for which
 `a + b + c = 1000`.
Find the product `abc`.


#### Solution: `31875000`
"""

from p009 import p009

SOLUTION = 31875000


def test_correctness():
    assert SOLUTION == p009()


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
