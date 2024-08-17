from dataclasses import dataclass


def reachable_by_3n_plus_1(m: int) -> bool:
    """
    An element m of the Collatz sequence can be reached by 3n + 1 if:
        1. (m - 1) is divisible by 3
        2. n is odd
        3. n is not 1

    is n is odd, then 3n will also be odd, therefore 2. <=> (m - 1) is odd
    n is 1 <=> m is 4
    """

    divisible = (m - 1) % 3 == 0
    odd = (m - 1) % 2 != 0
    nonterminal = m != 4

    return divisible and odd and nonterminal


def reverse_collatz(n: int) -> list[int]:
    res = [n * 2]

    if reachable_by_3n_plus_1(n):
        res += [(n - 1) // 3]

    return res


@dataclass
class CollatzNode:
    value: int
    parent: "CollatzNode | None"
    children: "list[CollatzNode] | None"


class CollatzTree:
    root: CollatzNode
    leaves: list[CollatzNode]
    coverage: list[int]

    def __init__(self) -> None:
        self.root = CollatzNode(
            value=1,
            parent=None,
            children=None,
        )
        self.leaves = [self.root]
        self.coverage = [self.root.value]

    def grow(self) -> None:
        new_leaves = []
        for leaf in self.leaves:
            leaf.children = [
                CollatzNode(v, leaf, None) for v in reverse_collatz(leaf.value)
            ]
            self.coverage = sorted(
                self.coverage + [node.value for node in leaf.children]
            )
            new_leaves += leaf.children
        self.leaves = new_leaves

    def generations(self) -> list[list[int]]:
        results = [[self.root]]
        while True:
            gen = []

            for n in results[-1]:
                if n.children is not None:
                    gen += n.children

            if len(gen) == 0:
                break

            results.append(gen)

        return [[leaf.value for leaf in leaves] for leaves in results]

    def sequences(self) -> list[list[int]]:
        sequences = [[self.root]]

        noop = False
        while not noop:
            noop = True
            new_sequences = []

            for seq in sequences:
                tip = seq[-1]

                if tip.children is None:
                    continue

                noop = False
                if len(tip.children) == 1:
                    seq += tip.children
                else:
                    # Otherwise we branch
                    branch = seq[:]
                    seq.append(tip.children[0])
                    branch.append(tip.children[1])
                    new_sequences.append(branch)

            sequences += new_sequences

        return [[node.value for node in nodes] for nodes in sequences]
