from euler.problems import (
    collatz,
    factors,
    fibonacci,
    flip_y,
    is_leap_year,
    number_word,
    primes,
    prime_factors,
    spiral_corners,
    uniq,
    windows,
    sieve,
    diagonals,
    transpose,
    bigsum,
    Fraction,
)
from itertools import islice, takewhile


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


def test_leap_years():
    assert not is_leap_year(1900)
    assert is_leap_year(1904)
    assert is_leap_year(1992)
    assert not is_leap_year(1993)
    assert is_leap_year(1996)
    assert is_leap_year(2000)


def test_uniq():
    test_list = [1, 1, 2, 4, 3, 1]
    assert list(uniq(test_list)) == [1, 2, 4, 3, 1]

    test_list = [1, 1, 2, 4, 4, 4, 3, 1]
    assert list(uniq(test_list)) == [1, 2, 4, 3, 1]


def test_factors_of_6():
    assert factors(6) == {1, 2, 3, 6}


def test_factors_of_12():
    assert factors(12) == {1, 2, 3, 4, 6, 12}


def test_factors_of_18():
    assert factors(18) == {1, 2, 3, 6, 9, 18}


def test_factors_of_600():
    assert factors(600) == {
        1,
        2,
        3,
        4,
        5,
        6,
        8,
        10,
        12,
        15,
        20,
        24,
        25,
        30,
        40,
        50,
        60,
        75,
        100,
        120,
        150,
        200,
        300,
        600,
    }


def test_fraction_half():
    half = Fraction(1, 2)

    assert half.whole_part == 0
    assert half.finite_part == [5]
    assert half.infinite_part == [0]


def test_fraction_eighth():
    eighth = Fraction(1, 8)

    assert eighth.whole_part == 0
    assert eighth.finite_part == [1, 2, 5]
    assert eighth.infinite_part == [0]


def test_fraction_third():
    third = Fraction(1, 3)

    assert third.whole_part == 0
    assert third.finite_part == []
    assert third.infinite_part == [3]


def test_fraction_annoying():
    annoying = Fraction(103, 300)

    assert annoying.whole_part == 0
    assert annoying.finite_part == [3, 4]
    assert annoying.infinite_part == [3]


def test_fraction_whole():
    whole = Fraction(30, 10)

    assert whole.whole_part == 3
    assert whole.finite_part == []
    assert whole.infinite_part == [0]


def test_fraction_seventh():
    seventh = Fraction(1, 7)

    assert seventh.whole_part == 0
    assert seventh.finite_part == []
    assert seventh.infinite_part == [1, 4, 2, 8, 5, 7]


def test_fraction_stringify():
    assert str(Fraction(1, 2)) == "0.5"
    assert str(Fraction(1, 8)) == "0.125"
    assert str(Fraction(1, 3)) == "0.(3)"
    assert str(Fraction(103, 300)) == "0.34(3)"
    assert str(Fraction(30, 10)) == "3"
    assert str(Fraction(1, 7)) == "0.(142857)"


def test_spiral_corners():
    assert [*takewhile(lambda x: x <= 25, spiral_corners())] == [
        1,
        3,
        5,
        7,
        9,
        13,
        17,
        21,
        25,
    ]
