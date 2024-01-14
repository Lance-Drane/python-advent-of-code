import sys
from itertools import pairwise

total = 0
for line in sys.stdin.readlines():
    ok = True
    for pair in pairwise(sorted(line.split())):
        if pair[0] == pair[1]:
            ok = False
            break
    if ok:
        total += 1

print(total)
