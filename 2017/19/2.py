# note that, with the exception of the single character at the top, the grid should be surrounded by spaces

import sys

grid = sys.stdin.read().splitlines()
y = 0
x = grid[0].index('|')
direction = 2
"""
0: up
1: right
2: down
3: left
"""

count = 1
while True:
    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    else:
        x -= 1

    next_char = grid[y][x]
    if next_char == ' ':
        break
    elif next_char == '+':
        direction = (1 if grid[y][x - 1] == ' ' else 3) if direction & 1 == 0 else 2 if grid[y - 1][x] == ' ' else 0

    count += 1

print(count)
