from euler.problems import fibonacci, primes, prime_factors, windows, sieve
from itertools import islice


def test_fibonacci():
    first_ten = list(islice(fibonacci(), 10))

    assert first_ten == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_primes():
    first_ten = list(islice(primes(), 10))

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
    assert list(windows(range(0, 10), 3)) == [
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
