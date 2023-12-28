from collections import deque

# you can play around with the next two values
# you'll want to be a bit bigger than the target values, but not too much bigger
COLUMNS = 39
ROWS = 41

ROW_TARGET = 39
COLUMN_TARGET = 31

UPPER_HEIGHT_BOUND = ROWS * COLUMNS - COLUMNS
grid = [False] * (COLUMNS * ROWS)

favorite_num = int(input())


def fill_grid_pos(x: int, y: int):
    return (x * x + 3 * x + 2 * x * y + y + y * y + favorite_num).bit_count() & 1 == 0


for y in range(ROWS):
    for x in range(COLUMNS):
        grid[y * COLUMNS + x] = fill_grid_pos(x, y)

start = COLUMNS + 1
end = COLUMNS * ROW_TARGET + COLUMN_TARGET
grid[start] = False
queue = deque([(0, start)])
while queue:
    count, curr_idx = queue.popleft()
    # top
    if curr_idx >= COLUMNS:
        top_idx = curr_idx - COLUMNS
        if top_idx == end:
            print(count + 1)
            break
        elif grid[top_idx]:
            grid[top_idx] = False
            queue.append((count + 1, top_idx))
    # right
    if curr_idx % COLUMNS != (COLUMNS - 1):
        right_idx = curr_idx + 1
        if right_idx == end:
            print(count + 1)
            break
        elif grid[right_idx]:
            grid[right_idx] = False
            queue.append((count + 1, right_idx))
    # bottom
    if curr_idx < UPPER_HEIGHT_BOUND:
        bottom_idx = curr_idx + COLUMNS
        if bottom_idx == end:
            print(count + 1)
            break
        elif grid[bottom_idx]:
            grid[bottom_idx] = False
            queue.append((count + 1, bottom_idx))
    # left
    if curr_idx % COLUMNS != 0:
        left_idx = curr_idx - 1
        if left_idx == end:
            print(count + 1)
            break
        elif grid[left_idx]:
            grid[left_idx] = False
            queue.append((count + 1, left_idx))
