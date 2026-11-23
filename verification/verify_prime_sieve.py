#!/usr/bin/env python3
"""Cross-check the eventual congruence criterion for the PII first obstruction.

Computes the first-obstruction root condition independently in the two forms:
(1) the product root set modulo the given prime;
(2) a finite residue-class rule.  The infinite claim is proved in the paper.
"""
from math import gcd, isqrt


def is_prime(p):
    return p > 1 and all(p % q for q in range(2, isqrt(p) + 1))


def direct_zero(a, b, p):
    assert p > 3 and gcd(p, b) == 1
    aa = (a * pow(b, -1, p)) % p
    r = p // 6
    return any(aa == (3 * j) % p for j in range(-r, r + 1))


def residue_classes(a, b):
    if b < 3:
        raise ValueError('use the special cases for b=1,2')
    M = 3 * b
    return {u for u in range(M) if gcd(u, M) == 1 and any((ell*u+a) % M == 0
            for ell in range(-b, b + 1) if 0 < 2*abs(ell) < b)}


def eventual_zero(a, b, p):
    if b == 1:
        return a % 3 == 0
    if b == 2:
        return (p - abs(a)) % 6 == 0
    return (p % (3*b)) in residue_classes(a, b)


def root_class_count_formula(a, b):
    if b < 3:
        raise ValueError('not a b>=3 formula')
    if a % 3:
        return 2 * sum(gcd(ell, 3*b) == 1 for ell in range(1, b) if 2*ell < b)
    return 4 * sum(gcd(m, b) == 1 for m in range(1, b) if 6*m < b)


def main():
    primes = [p for p in range(5, 601) if is_prime(p)]
    count = 0
    examples = 0
    for b in range(1, 31):
        for a in range(-35, 36):
            if gcd(a, b) != 1:
                continue
            if b >= 3:
                actual_count = len(residue_classes(a,b))
                expected_count = root_class_count_formula(a,b)
                assert actual_count == expected_count, (a,b, actual_count, expected_count)
                examples += 1
            bound = max(3, 2*abs(a)+(5*b if b>=3 else 0))
            for p in primes:
                if p <= bound or gcd(p, b) != 1:
                    continue
                actual = direct_zero(a, b, p)
                expected = eventual_zero(a, b, p)
                assert actual == expected, (a,b,p,actual,expected)
                count += 1
    print(f'eventual periodicity: {count} prime/parameter checks')
    print(f'exact residue counts: {examples} coprime parameters b>=3')
    from fractions import Fraction as F
    # Examples: first-obstruction *bad*-prime densities.
    samples = [(1,2,F(1,2)),(3,2,F(1)),(1,3,F(2,3)),(1,4,F(1,2)),(3,7,F(2,3)),(3,5,F(1))]
    for a,b,expected_bad in samples:
        if b==2:
            density_bad=F(1 if a%3==0 else 1, 1 if a%3==0 else 2)
        else:
            modulus=3*b
            phi=sum(gcd(u,modulus)==1 for u in range(modulus))
            density_bad=F(phi-len(residue_classes(a,b)),phi)
        assert density_bad==expected_bad, (a,b,density_bad,expected_bad)
    print('sample prime densities: six cases verified exactly')

if __name__ == '__main__':
    main()
