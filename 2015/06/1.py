import re
import sys

lights = [[False for i in range(1000)] for j in range(1000)]

for line in sys.stdin.readlines():
    pattern = re.search(r'([a-z]+) (\d+),(\d+) through (\d+),(\d+)$', line)
    instruction = pattern.group(1)
    a = int(pattern.group(2))
    b = int(pattern.group(3))
    c = int(pattern.group(4)) + 1
    d = int(pattern.group(5)) + 1

    if instruction == 'toggle':
        for x in range(a, c):
            for y in range(b, d):
                lights[x][y] = not lights[x][y]
    elif instruction == 'off':
        for x in range(a, c):
            for y in range(b, d):
                lights[x][y] = False
    else:
        for x in range(a, c):
            for y in range(b, d):
                lights[x][y] = True

print(sum(r.count(True) for r in lights))
