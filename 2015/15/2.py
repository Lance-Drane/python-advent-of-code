import re
import sys
from math import prod


def combos():
    for a in range(100):
        for b in range(100 - a):
            for c in range(100 - a - b):
                yield a, b, c, 100 - a - b - c


ingredients = tuple(tuple(int(a.group()) for a in re.finditer(r'-?\d+', line)) for line in sys.stdin.readlines())

print(
    max(
        prod(
            (max(0, sum(b[0] * b[1] for b in zip((a[i] for a in ingredients), tsps, strict=False))) for i in range(4)),
        )
        for tsps in filter(
            lambda perm: sum(b[0] * b[1] for b in zip((a[4] for a in ingredients), perm, strict=False)) == 500,
            combos(),
        )
    )
)
