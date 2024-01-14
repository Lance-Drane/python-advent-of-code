import sys
from itertools import combinations

total = 0
for line in sys.stdin.readlines():
    for combo in combinations(sorted(map(int, line.split())), 2):
        if combo[1] % combo[0] == 0:
            total += combo[1] // combo[0]
            break

print(total)
