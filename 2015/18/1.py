import sys
from itertools import chain

GRID_SIZE = 100
STEPS = 100


def neighbors(point):
    x, y = point
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1
    yield x + 1, y - 1
    yield (
        x + 1,
        y + 1,
    )
    yield x - 1, y - 1
    yield x - 1, y + 1


def advance(board):
    new = set()
    recal = board | set(
        filter(
            lambda p: p[0] < GRID_SIZE and p[0] >= 0 and p[1] < GRID_SIZE and p[1] >= 0, chain(*map(neighbors, board))
        )
    )
    for point in recal:
        count = sum((neigh in board) for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            new.add(point)
    return new


grid = set()

for l_idx, line in enumerate(sys.stdin.readlines()):
    for p_idx, point in enumerate(line):
        if point == '#':
            grid.add((l_idx, p_idx))

for _ in range(STEPS):
    grid = advance(grid)

print(len(grid))
