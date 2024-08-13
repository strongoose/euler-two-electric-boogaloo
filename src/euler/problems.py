from typing import Iterator
from itertools import takewhile


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
        [n for n in takewhile(lambda x: x < 4_000_000, fibonacci()) if n % 2 == 0]
    )
