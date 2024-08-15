import time
from typing import TypeVar, Callable
from . import problems
from tabulate import tabulate

T = TypeVar("T")


def timed(f: Callable[[], T]) -> tuple[int, T]:
    start = time.time_ns()
    res = f()
    elapsed = time.time_ns() - start
    ms = elapsed // 1000
    return ms, res


def all_problems() -> list[Callable[[], int]]:
    ps, n = [], 1
    try:
        while True:
            ps.append(getattr(problems, f"p{n}"))
            n += 1
    except AttributeError:
        pass
    return ps


def main() -> int:
    ps = all_problems()

    results = [timed(p) for p in ps]
    pretty = [
        [i+1, f'{ms:,}ms', f'{result:,}'] for i, (ms, result) in enumerate(results)
    ]

    print(tabulate(pretty, stralign='right'))

    return 0
