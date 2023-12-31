NUM_ROWS = 40

grid = [input()]

while len(grid) < NUM_ROWS:
    row = grid[-1]

    next_row = [
        '^' if row[1] == '^' else '.',
        *('^' if row[idx - 1] != row[idx + 1] else '.' for idx in range(1, len(row) - 1)),
        '^' if row[-2] == '^' else '.',
    ]

    grid.append(''.join(next_row))

print(''.join(grid).count('.'))
