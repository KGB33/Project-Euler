from p005 import p005, gcd, lcm


SOLUTION = 232792560


def test_correctness():
    assert SOLUTION == p005()


def test_lcm():
    assert 11461 == lcm(157, 73)
    assert 15 == lcm(15, 5)
    assert 15 == lcm(5, 15)
    assert 32 == lcm(32, 32)
    assert 232 == lcm(58, 8)


def test_gcd():
    assert 1 == gcd(157, 73)
    assert 5 == gcd(15, 5)
    assert 5 == gcd(5, 15)
    assert 32 == gcd(32, 32)
