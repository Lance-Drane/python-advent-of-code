import sys

total = 0
for line in sys.stdin.readlines():
    vals = sorted(map(int, line.split()))
    total += vals[-1] - vals[0]

print(total)
