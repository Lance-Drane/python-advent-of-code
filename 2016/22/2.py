import re
import sys
from collections import deque

nodes = sys.stdin.readlines()[2:]
grid_size = int(len(nodes) ** 0.5)
max_used_size = float('inf')
start_position = (-1, -1)
used_node_map = [[None for _ in range(grid_size)] for _ in range(grid_size)]

for line in nodes:
    x, y, size, used, avail, use_percent = map(int, re.findall(r'\d+', line))
    if used == 0:
        max_used_size = size
        start_position = (y, x)
    used_node_map[y][x] = used

# use bfs to compute how many steps it takes to get to the node to the left of the goal node
target_position = (0, grid_size - 2)
queue = deque([(0, start_position)])
visited = {start_position}
while queue:
    count, curr_position = queue.popleft()
    if curr_position == target_position:
        break
    if used_node_map[curr_position[0]][curr_position[1]] > max_used_size:
        continue
    # top
    if curr_position[0] > 0:
        next_position = (curr_position[0] - 1, curr_position[1])
        if next_position not in visited:
            visited.add(next_position)
            queue.append((count + 1, next_position))
    # right
    if curr_position[1] < grid_size - 1:
        next_position = (curr_position[0], curr_position[1] + 1)
        if next_position not in visited:
            visited.add(next_position)
            queue.append((count + 1, next_position))
    # bottom
    if curr_position[0] < grid_size - 1:
        next_position = (curr_position[0] + 1, curr_position[1])
        if next_position not in visited:
            visited.add(next_position)
            queue.append((count + 1, next_position))
    # left
    if curr_position[1] > 0:
        next_position = (curr_position[0], curr_position[1] - 1)
        if next_position not in visited:
            visited.add(next_position)
            queue.append((count + 1, next_position))

# this should work as long as the top row has no oversized values
print(count + (grid_size - 2) * 5 + 1)
