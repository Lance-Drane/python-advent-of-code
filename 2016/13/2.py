from collections import deque

# you can play around with the next two values
# you'll want to be a bit bigger than the target values, but not too much bigger
COLUMNS = 52
ROWS = 52

UPPER_HEIGHT_BOUND = ROWS * COLUMNS - COLUMNS
grid = [False] * (COLUMNS * ROWS)

favorite_num = int(input())


def fill_grid_pos(x: int, y: int):
    return (x * x + 3 * x + 2 * x * y + y + y * y + favorite_num).bit_count() & 1 == 0


for y in range(ROWS):
    for x in range(COLUMNS):
        grid[y * COLUMNS + x] = fill_grid_pos(x, y)

start = COLUMNS + 1
grid[start] = False
queue = deque([(0, start)])
total = 0
while queue:
    count, curr_idx = queue.popleft()
    if count == 51:
        break
    total += 1
    # top
    if curr_idx >= COLUMNS:
        top_idx = curr_idx - COLUMNS
        if grid[top_idx]:
            grid[top_idx] = False
            queue.append((count + 1, top_idx))
    # right
    if curr_idx % COLUMNS != (COLUMNS - 1):
        right_idx = curr_idx + 1
        if grid[right_idx]:
            grid[right_idx] = False
            queue.append((count + 1, right_idx))
    # bottom
    if curr_idx < UPPER_HEIGHT_BOUND:
        bottom_idx = curr_idx + COLUMNS
        if grid[bottom_idx]:
            grid[bottom_idx] = False
            queue.append((count + 1, bottom_idx))
    # left
    if curr_idx % COLUMNS != 0:
        left_idx = curr_idx - 1
        if grid[left_idx]:
            grid[left_idx] = False
            queue.append((count + 1, left_idx))

print(total)
