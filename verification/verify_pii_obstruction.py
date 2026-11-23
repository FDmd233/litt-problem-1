#!/usr/bin/env python3
"""Exact-arithmetic checks for the first Painleve-II obstruction polynomial.

The script checks finite ranges only. The all-prime statements are proved in
paper/main.tex and are not inferred from these computations.
Only the Python standard library is required.
"""
from fractions import Fraction
from math import comb, factorial, isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def poly_trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a, b, p):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] = (c[i] + x) % p
    for i, x in enumerate(b):
        c[i] = (c[i] + x) % p
    return poly_trim(c, p)


def poly_mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    return poly_trim(c, p)


def poly_scale(a, scalar, p):
    return poly_trim([scalar * x for x in a], p)


def obstruction_from_recurrence(p):
    """Compute H_p(A) directly from the coefficient recurrence in F_p[A]."""
    m = p // 3
    b = []
    squares = []
    for k in range(m + 1):
        rhs = [0, 1] if k == 0 else b[k - 1][:]
        if k >= 2:
            for i in range(k - 1):
                rhs = poly_add(
                    rhs,
                    poly_scale(poly_mul(squares[i], b[k - 2 - i], p), 2, p),
                    p,
                )
        if k == m:
            denominator = (3 * k + 1) * (3 * k + 2)
            unit_part = denominator // p
            return poly_scale(rhs, pow(unit_part, -1, p), p)
        denominator = ((3 * k + 1) * (3 * k + 2)) % p
        bk = poly_scale(rhs, pow(denominator, -1, p), p)
        b.append(bk)
        square_k = [0]
        for i in range(k + 1):
            square_k = poly_add(square_k, poly_mul(b[i], b[k - i], p), p)
        squares.append(square_k)
    raise AssertionError("unreachable")


def obstruction_formula(p):
    r = p // 6
    if p % 6 == 1:
        constant = ((-1) ** (r + 1) * comb(2 * r, r)) % p
    else:
        constant = (2 * (-1) ** r * comb(2 * r, r)) % p
    result = [0, constant]
    for j in range(1, r + 1):
        result = poly_mul(result, [(-9 * j * j) % p, 0, 1], p)
    return result


def ordinary_series(alpha, degree):
    """Exact Taylor coefficients for y''=2y^3+t*y+alpha, y(0)=y'(0)=0."""
    a = [Fraction(0) for _ in range(degree + 1)]
    squares = [Fraction(0) for _ in range(degree + 1)]
    for n in range(degree - 1):
        squares[n] = sum(a[i] * a[n - i] for i in range(n + 1))
        cube = sum(squares[i] * a[n - i] for i in range(n + 1))
        rhs = 2 * cube + (a[n - 1] if n else alpha)
        a[n + 2] = rhs / ((n + 1) * (n + 2))
    return a


def main():
    primes = [p for p in range(5, 301) if is_prime(p)]
    for p in primes:
        actual = obstruction_from_recurrence(p)
        expected = obstruction_formula(p)
        assert actual == expected, (p, actual, expected)
    print(f"H_p identity: {len(primes)} primes, 5 <= p <= 300")

    coefficients = ordinary_series(Fraction(1), 800)
    for p in [q for q in range(5, 100) if is_prime(q)]:
        first_bad = next(i for i, c in enumerate(coefficients) if c.denominator % p == 0)
        expected = p if p % 6 == 5 else p + 1
        assert first_bad == expected, (p, first_bad, expected)
        value = p * coefficients[first_bad]
        assert value.denominator % p != 0
        assert value.numerator % p != 0
        r = p // 6
        factor = comb(2 * r, r) * factorial(3 * r + 1)
        factor *= pow((3 ** r * factorial(r)) % p, -1, p)
        expected_residue = (-factor if p % 6 == 1 else 2 * factor) % p
        actual_residue = (value.numerator * pow(value.denominator, -1, p)) % p
        assert actual_residue == expected_residue, (p, actual_residue, expected_residue)
    print("A=1 first bad index, valuation -1, and residue: all primes 5 <= p <= 97")

    assert coefficients[2] == Fraction(1, 2)
    print("A=1, p=2: first bad index is 2")

    # The support restriction and 3-integrality are checked to the same degree.
    assert all(c == 0 for i, c in enumerate(coefficients) if i % 3 != 2)
    assert all(c.denominator % 3 != 0 for c in coefficients)
    print("Support and 3-integrality: checked through degree 800")


if __name__ == "__main__":
    main()
