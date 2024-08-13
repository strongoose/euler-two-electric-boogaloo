from typing import Iterator, Iterable

import itertools as it
from math import sqrt, floor


def p1() -> int:
    return sum([n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0])


def fibonacci() -> Iterator[int]:
    prev: int = 1
    yield prev
    curr: int = 1
    yield curr
    while True:
        curr, prev = curr + prev, curr
        yield curr


def p2() -> int:
    return sum(
        [n for n in it.takewhile(lambda x: x < 4_000_000, fibonacci()) if n % 2 == 0]
    )


def primes() -> Iterator[int]:
    primes = [2]
    yield 2

    def isprime(n: int) -> bool:
        return all(map(lambda p: n % p != 0, primes))

    i = 3
    while True:
        if isprime(i):
            primes.append(i)
            yield i
        i += 2


def prime_factors(n: int) -> list[int]:
    dividend = n
    factors = []

    for p in it.takewhile(lambda x: x <= sqrt(dividend), primes()):
        while dividend % p == 0:
            dividend = dividend // p
            factors.append(p)

    # The remaining dividend is the last prime factor
    # This can be 1 sometimes - for example, finding the prime factors of 4
    if dividend != 1:
        factors.append(dividend)
    return factors


def p3() -> int:
    return prime_factors(600851475143)[-1]


def is_palindrome(n: int) -> bool:
    word = str(n)

    while word != "":
        if word[0] != word[-1]:
            return False

        word = word[1:-1]

    return True


def p4() -> int:
    max = 0

    for a in range(1, 1000):
        for b in range(1, 1000):
            product = a * b
            if product > max and is_palindrome(product):
                max = a * b

    return max


def product(ns: Iterable[int]) -> int:
    res = 1
    for n in ns:
        res = res * n
    return res


def p5() -> int:
    """
    My intuition was wrong with this one - initially I thought we could just take all the primes under 20 and multiply them... but if we do that the result won't divide by, e.g., 4 (== 2 * 2)
    """
    factors = []

    for p in it.takewhile(lambda x: x < 20, primes()):
        # We add this prime factor n times, where n is the largest integer for which factor**n < 20
        # i.e., the floor of the nth root of 20
        repeats = floor(20 ** (1 / p))

        for _ in range(0, repeats):
            factors.append(p)

    return product(factors)


def p6() -> int:
    sum_of_squares = sum([n**2 for n in range(0, 101)])
    square_of_sum = sum(range(0, 101)) ** 2

    return square_of_sum - sum_of_squares
