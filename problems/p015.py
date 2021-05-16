"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20×20 grid?
"""

"""
Note: this can be solved using Binomial Coefficients (nCk), aka n choose k.

For the 2x2 example we have:
     _ _ _ _  spots and R, R, D, D to choose from

however, once all the R's or all the D's are in place, the other must fill in
the blanks, thus we have 4C2

nCk =  ___(n!)___
       k!(n - k!)
"""
import time

SOLUTION = 137846528820


def main():
    size = 20
    n = size * 2
    k = size
    return comb(n, k, exact=True)


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta


def comb(N, k, exact=False, repetition=False):
    """
    === Vendor-ed from https://github.com/scipy/scipy/blob/v1.6.3/scipy/special/_basic.py#L2140-L2198 ===
    The number of combinations of N things taken k at a time.
    This is often expressed as "N choose k".
    Parameters
    ----------
    N : int, ndarray
        Number of things.
    k : int, ndarray
        Number of elements taken.
    exact : bool, optional
        If `exact` is False, then floating point precision is used, otherwise
        exact long integer is computed.
    repetition : bool, optional
        If `repetition` is True, then the number of combinations with
        repetition is computed.
    Returns
    -------
    val : int, float, ndarray
        The total number of combinations.
    See Also
    --------
    binom : Binomial coefficient ufunc
    Notes
    -----
    - Array arguments accepted only for exact=False case.
    - If N < 0, or k < 0, then 0 is returned.
    - If k > N and repetition=False, then 0 is returned.
    Examples
    --------
    >>> from scipy.special import comb
    >>> k = np.array([3, 4])
    >>> n = np.array([10, 10])
    >>> comb(n, k, exact=False)
    array([ 120.,  210.])
    >>> comb(10, 3, exact=True)
    120
    >>> comb(10, 3, exact=True, repetition=True)
    220
    """
    if repetition:
        return comb(N + k - 1, k, exact)
    if exact:
        return _comb_int(N, k)
    else:
        k, N = asarray(k), asarray(N)
        cond = (k <= N) & (N >= 0) & (k >= 0)
        vals = binom(N, k)
        if isinstance(vals, np.ndarray):
            vals[~cond] = 0
        elif not cond:
            vals = np.float64(0)
        return vals


def _comb_int(N, k):
    N = int(N)
    k = int(k)

    if k > N or N < 0 or k < 0:
        return 0

    M = N + 1
    nterms = min(k, N - k)

    numerator = 1
    denominator = 1
    for j in range(1, nterms + 1):
        numerator *= M - j
        denominator *= j

    return numerator // denominator
