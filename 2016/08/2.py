import sys

ROWS = 6
COLUMNS = 50

grid = [['.' for i in range(COLUMNS)] for j in range(ROWS)]

for line in sys.stdin.readlines():
    parts = line.split(' ')

    # rectangle
    if parts[0] == 'rect':
        cols, rows = map(int, parts[1].split('x'))
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = '#'
        continue

    # rotation
    amount = int(parts[4])
    target = int(parts[2].split('=')[1])

    if parts[1] == 'row':
        grid[target] = grid[target][(-amount):] + grid[target][:(-amount)]
    else:
        column = [grid[i][target] for i in range(ROWS)]
        column = column[(-amount):] + column[:(-amount)]
        for i in range(ROWS):
            grid[i][target] = column[i]

# note that the actual output is in ASCII, the literal stdout submission doesn't work here!
for row in grid:
    print(''.join(row))
