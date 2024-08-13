from euler.problems import fibonacci
from itertools import islice


def test_fibonacci():
    first_ten = list(islice(fibonacci(), 10))

    assert first_ten == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
