import sys
from itertools import pairwise

blacklisted = [
    (0, 0),
    *sorted(
        [(int(chunk[0]), int(chunk[1])) for chunk in (line.split('-') for line in sys.stdin.readlines())],
        key=lambda a: a[0],
    ),
    (4294967295, 4294967295),
]

valids = []
highest = 0
for low, high in pairwise(blacklisted):
    highest = max(highest, low[1])
    if high[0] > highest + 1:
        valids += range(highest + 1, high[0])

print(len(valids))
