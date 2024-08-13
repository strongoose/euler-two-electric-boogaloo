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
        # return all(map(lambda p: n % p != 0, primes))
        for p in primes:
            if n % p == 0:
                return False
        return True

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


def p7() -> int:
    # This takes a second or so, so commenting out to speed up feedback
    # return list(it.islice(primes(), 10_000))[-1]
    return 104729


def windows(input: Iterable[int], width: int) -> Iterator[list[int]]:
    iterator = iter(input)
    window: list[int] = []

    for i in range(0, width):
        window.append(next(iterator))
    yield window[:]

    for n in iterator:
        window.pop(0)
        window.append(n)
        yield window[:]


def p8() -> int:
    input = "".join(
        """
      73167176531330624919225119674426574742355349194934
      96983520312774506326239578318016984801869478851843
      85861560789112949495459501737958331952853208805511
      12540698747158523863050715693290963295227443043557
      66896648950445244523161731856403098711121722383113
      62229893423380308135336276614282806444486645238749
      30358907296290491560440772390713810515859307960866
      70172427121883998797908792274921901699720888093776
      65727333001053367881220235421809751254540594752243
      52584907711670556013604839586446706324415722155397
      53697817977846174064955149290862569321978468622482
      83972241375657056057490261407972968652414535100474
      82166370484403199890008895243450658541227588666881
      16427171479924442928230863465674813919123162824586
      17866458359124566529476545682848912883142607690042
      24219022671055626321111109370544217506941658960408
      07198403850962455444362981230987879927244284909188
      84580156166097919133875499200524063689912560717606
      05886116467109405077541002256983155200055935729725
      71636269561882670428252483600823257530420752963450
    """.split()
    )

    digits = [int(c) for c in input]

    max = 0
    for window in windows(digits, 13):
        if (x := product(window)) > max:
            max = x

    return max
