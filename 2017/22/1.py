import sys

BURSTS = 10_000

grid_str = sys.stdin.read().split()
grid = set()

for row_idx, row in enumerate(grid_str):
    for col_idx, val in enumerate(row):
        if val == '#':
            grid.add((row_idx, col_idx))

grid_midpoint = len(grid_str[0]) >> 1

position = (grid_midpoint, grid_midpoint)
facing = 0
"""
0 = UP
1 = RIGHT
2 = DOWN
3 = LEFT
"""

infections = 0

for _ in range(BURSTS):
    if position in grid:
        grid.remove(position)
        facing = 0 if facing == 3 else facing + 1
    else:
        grid.add(position)
        facing = 3 if facing == 0 else facing - 1
        infections += 1
    if facing == 0:
        position = (position[0] - 1, position[1])
    elif facing == 1:
        position = (position[0], position[1] + 1)
    elif facing == 2:
        position = (position[0] + 1, position[1])
    else:
        position = (position[0], position[1] - 1)

print(infections)
