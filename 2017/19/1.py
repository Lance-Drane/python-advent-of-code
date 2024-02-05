# note that, with the exception of the single character at the top, the grid should be surrounded by spaces

import sys

grid = sys.stdin.read().splitlines()
position = (0, 0)
direction = 2
"""
0: up
1: right
2: down
3: left
"""

for idx, char in enumerate(grid[0]):
    if char == '|':
        position = (0, idx)
        break

out = []
while True:
    if direction == 0:
        position = (position[0] - 1, position[1])
    elif direction == 1:
        position = (position[0], position[1] + 1)
    elif direction == 2:
        position = (position[0] + 1, position[1])
    else:
        position = (position[0], position[1] - 1)

    next_char = grid[position[0]][position[1]]
    if next_char == ' ':
        break
    elif next_char == '+':
        if direction & 1 == 0:  # vertical
            direction = 1 if grid[position[0]][position[1] - 1] == ' ' else 3
        else:  # horiziontal
            direction = 2 if grid[position[0] - 1][position[1]] == ' ' else 0
    elif next_char in ('-', '|'):
        pass
    else:
        out.append(next_char)

print(''.join(out))
