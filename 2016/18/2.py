NUM_ROWS = 400000

grid = [input()]

while len(grid) < NUM_ROWS:
    row = grid[-1]

    # initialize with leftmost char
    next_row = ['^' if row[1] == '^' else '.']

    # middle tiles
    next_row.extend('^' if row[idx - 1] != row[idx + 1] else '.' for idx in range(1, len(row) - 1))

    # rightmost
    next_row.append('^' if row[-2] == '^' else '.')

    grid.append(''.join(next_row))

print(''.join(grid).count('.'))
