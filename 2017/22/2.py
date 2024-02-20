import sys

BURSTS = 10_000_000

grid_str = sys.stdin.read().split()
grid: dict[tuple[int, int], int] = {}
"""
not in grid = CLEAN
1 = WEAKENED
2 = INFECTED
3 = FLAGGED
"""

for row_idx, row in enumerate(grid_str):
    for col_idx, val in enumerate(row):
        if val == '#':
            grid[(row_idx, col_idx)] = 2

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
    position_state = grid.get(position)
    if position_state is None:  # CLEAN
        grid[position] = 1
        facing = 3 if facing == 0 else facing - 1
    elif position_state == 1:  # WEAKENED
        grid[position] = 2
        infections += 1
    elif position_state == 2:  # INFECTED
        grid[position] = 3
        facing = 0 if facing == 3 else facing + 1
    else:  # FLAGGED
        del grid[position]
        facing = facing + 2 if facing < 2 else facing - 2

    if facing == 0:
        position = (position[0] - 1, position[1])
    elif facing == 1:
        position = (position[0], position[1] + 1)
    elif facing == 2:
        position = (position[0] + 1, position[1])
    else:
        position = (position[0], position[1] - 1)

print(infections)
