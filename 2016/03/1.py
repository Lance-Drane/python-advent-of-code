import re
import sys

count = 0
for line in sys.stdin.readlines():
    sides = sorted(int(a.group(0)) for a in re.finditer(r'[\d]+', line))
    if sides[0] + sides[1] > sides[2]:
        count += 1

print(count)
