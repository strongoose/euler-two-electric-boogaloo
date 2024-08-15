import sys
import time
from typing import TypeVar, Callable
from typing_extensions import NamedTuple
from . import problems
from tabulate import tabulate

T = TypeVar("T")


def timed(f: Callable[[], T]) -> tuple[int, T]:
    start = time.time_ns()
    res = f()
    elapsed = time.time_ns() - start
    ms = elapsed // 1000
    return ms, res


Problem = NamedTuple(
    "Problem",
    (
        ("n", int),
        ("fn", Callable[[], int]),
    ),
)


def p(n: int) -> Problem:
    fn: Callable[[], int] = getattr(problems, f"p{n}")
    return Problem(n, fn)


def all_problems() -> list[Problem]:
    ps, n = [], 1
    try:
        while True:
            ps.append(p(n))
            n += 1
    except AttributeError:
        pass
    return ps


def pretty_print(ps: list[Problem]) -> None:
    pretty = []

    for p in ps:
        ms, res = timed(p.fn)
        pretty.append([p.n, f"{ms:,}ms", f"{res:,}"])

    print(tabulate(pretty, stralign="right"))


def main() -> int:
    ps: list[Problem]

    if len(sys.argv) > 1:
        try:
            ps = [p(int(pn)) for pn in sys.argv[1:]]
        except AttributeError as e:
            print(e)
            sys.exit(1)
    else:
        ps = all_problems()

    pretty_print(ps)

    return 0
