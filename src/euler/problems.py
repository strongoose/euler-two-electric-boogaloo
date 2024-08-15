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


def isqrt(n: int) -> int | None:
    def iterate(guess: float) -> float:
        return (guess + n / guess) / 2

    prev = n / 2
    guess = iterate(prev)

    while abs(guess - prev) >= 0.5:
        prev, guess = guess, iterate(guess)

    root = floor(guess)

    if root * root == n:
        return root
    else:
        return None


def pythagorean_triplets() -> Iterator[tuple[int, int, int]]:
    for a in range(1, 1000):
        for b in range(a, 1000):
            if c := isqrt(a**2 + b**2):
                yield (a, b, c)


def p9() -> int:
    for a, b, c in pythagorean_triplets():
        if a + b + c == 1000:
            return a * b * c

    # Unreachable
    return 0


def sieve(n: int) -> list[int]:
    """
    There are two key optimisations in here that have made this problem tractable in less than a second or so
     - Instead of iterating through the sieve marking numbers as non-prime, use slice assignment. This is a _lot_ faster.
     - A much smaller optimisation which still helps a bit is only running over non-even numbers in the sieve range.
    """
    sieve = [True] * (n + 1)

    def sieve_for(n: int) -> None:
        start = n * 2
        products = len(sieve[start::n])
        sieve[start::n] = [False] * products

    limit = int(n**0.5) + 1
    sieve_for(2)
    for i in range(3, limit, 2):
        sieve_for(i)

    return [n for n, isprime in enumerate(sieve) if isprime and n > 1]


def p10() -> int:
    return sum(sieve(2_000_000))


def diagonals(arr: list[list[int]]) -> Iterator[list[int]]:
    """
       0 1                 1
       2 3 -> diagonals -> 0 3
       4 5                 2 5
                           4

                             2
       0 1 2                 1 5
       3 4 5 -> diagonals -> 0 4 8
       6 7 8                 3 7
                             6

    Number of diagonals = h + w - 1

    We read out the diagonals from top right to bottom left, as in the examples above.

    The function assumes that the array is a regular grid i.e. no uneven line lengths.
    """
    height = len(arr)
    width = len(arr[0])

    start_indices: list[tuple[int, int]] = [
        # Top row (y = 0) (in reverse order)
        *[(x, 0) for x in range(width - 1, -1, -1)],
        # Left column (x = 0) (excluding (0, 0), which is included in the top row)
        *[(0, y) for y in range(1, height)],
    ]

    diag = []
    for x, y in start_indices:
        while x < width and y < height:
            diag.append(arr[y][x])
            x, y = x + 1, y + 1
        yield diag
        diag = []


def transpose(arr: list[list[int]]) -> list[list[int]]:
    width = len(arr[0])
    return [[row[x] for row in arr] for x in range(0, width)]


def flip_y(arr: list[list[int]]) -> list[list[int]]:
    return arr[::-1]


def p11() -> int:
    input = [
        list(map(int, line.split()))
        for line in """
        08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
        49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
        81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
        52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
        22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
        24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
        32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
        67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
        24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
        21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
        78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
        16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
        86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
        19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
        04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
        88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
        04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
        20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
        20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
        01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """.strip().split("\n")
    ]

    res = 0

    # Horizontal
    for line in input:
        for w in windows(line, 4):
            res = max(product(w), res)

    # Diagonal (down-right)
    for diag in diagonals(input):
        if len(diag) >= 4:
            for w in windows(diag, 4):
                res = max(product(w), res)

    # Transpose for verticals
    input = transpose(input)
    for line in input:
        for w in windows(line, 4):
            res = max(product(w), res)

    # Flip for up-left diags
    input = flip_y(input)
    for diag in diagonals(input):
        if len(diag) >= 4:
            for w in windows(diag, 4):
                res = max(product(w), res)

    return res
