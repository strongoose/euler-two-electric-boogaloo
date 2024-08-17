from euler.problems import (
    collatz,
    fibonacci,
    flip_y,
    number_word,
    primes,
    prime_factors,
    windows,
    sieve,
    diagonals,
    transpose,
    bigsum,
)
from itertools import islice


def test_fibonacci():
    first_ten = [*islice(fibonacci(), 10)]

    assert first_ten == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_primes():
    first_ten = [*islice(primes(), 10)]

    print(first_ten)
    assert first_ten == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_prime_factors_of_4():
    assert prime_factors(4) == [2, 2]


def test_prime_factors_of_12():
    assert prime_factors(12) == [2, 2, 3]


def test_prime_factors_of_p3():
    assert prime_factors(600851475143) == [71, 839, 1471, 6857]


def test_prime_factors_of_another_random_big_n():
    assert prime_factors(109699210) == [2, 5, 10969921]


# This one takes a couple of seconds
# def test_prime_factors_of_another_random_bigger_n():
#     assert prime_factors(5165787440756484) == [2, 2, 3, 3, 29, 126631, 39074731]


def test_windows():
    assert [*windows(range(0, 10), 3)] == [
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
    ]


def test_sieve_4():
    up_to_4 = [2, 3]
    assert sieve(4) == up_to_4


def test_sieve_10():
    up_to_10 = [2, 3, 5, 7]
    assert sieve(10) == up_to_10


def test_sieve_30():
    up_to_30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert sieve(30) == up_to_30


def test_sieve_100():
    up_to_100 = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    assert sieve(100) == up_to_100


def test_square_diagonals():
    arr = [
        [0, 1],
        [2, 3],
    ]

    assert [*diagonals(arr)] == [[1], [0, 3], [2]]


def test_wide_diagonals():
    arr = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
    ]

    assert [*diagonals(arr)] == [[3], [2, 7], [1, 6], [0, 5], [4]]


def test_tall_diagonals():
    arr = [
        [0, 1],
        [2, 3],
        [4, 5],
        [6, 7],
    ]

    assert [*diagonals(arr)] == [[1], [0, 3], [2, 5], [4, 7], [6]]


def test_square_transpose():
    arr = [
        [0, 1],
        [2, 3],
    ]

    assert transpose(arr) == [
        [0, 2],
        [1, 3],
    ]


def test_wide_transpose():
    arr = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
    ]

    assert transpose(arr) == [
        [0, 4],
        [1, 5],
        [2, 6],
        [3, 7],
    ]


def test_tall_transpose():
    arr = [
        [0, 1],
        [2, 3],
        [4, 5],
        [6, 7],
    ]

    assert transpose(arr) == [
        [0, 2, 4, 6],
        [1, 3, 5, 7],
    ]


def test_transpose_is_reversible():
    arr = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15],
        [16, 17, 18, 19],
    ]

    assert transpose(transpose(arr)) == arr


def test_flip():
    arr = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
    ]

    assert flip_y(arr) == [
        [7, 8],
        [5, 6],
        [3, 4],
        [1, 2],
    ]


def test_not_so_bigsum():
    numbers = [12, 34, 28, 50]
    ns = [[int(digit) for digit in str(number).split()] for number in numbers]
    expected_result = [int(digit) for digit in str(sum(numbers))]

    assert bigsum(*ns) == expected_result


def test_collatz():
    assert [*collatz(13)] == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_number_word_123():
    assert number_word(123) == "one hundred and twenty three"


def test_number_word_1():
    assert number_word(1) == "one"


def test_number_word_1000():
    assert number_word(1000) == "one thousand"


def test_number_word_729():
    assert number_word(729) == "seven hundred and twenty nine"


def test_number_word_16():
    assert number_word(16) == "sixteen"


def test_number_word_zero():
    assert number_word(0) == "too small!"


def test_number_word_1001():
    assert number_word(1001) == "too big!"

def test_number_word_100():
    assert number_word(100) == "one hundred"

def test_number_word_400():
    assert number_word(400) == "four hundred"

def test_number_word_80():
    assert number_word(80) == "eighty"
