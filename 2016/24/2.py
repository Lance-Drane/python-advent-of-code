import sys
from collections import defaultdict, deque
from collections.abc import Generator
from itertools import pairwise, permutations

grid = sys.stdin.readlines()
graph: defaultdict[str, dict[str, int]] = defaultdict(dict)


def get_initial_positions() -> Generator[tuple[int, int], None, None]:
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            if char.isdigit():
                yield row_idx, col_idx


def bfs_update_graph(start: tuple[int, int]):
    start_char = grid[start[0]][start[1]]
    queue = deque([(0, start)])
    visited = {start}
    while queue:
        count, curr_position = queue.popleft()
        # note that my input has a border of walls, so I skip some control flow checks
        for next_position in (
            (curr_position[0] - 1, curr_position[1]),
            (curr_position[0], curr_position[1] + 1),
            (curr_position[0] + 1, curr_position[1]),
            (curr_position[0], curr_position[1] - 1),
        ):
            if next_position not in visited:
                point = grid[next_position[0]][next_position[1]]
                if point != '#':
                    next_count = count + 1
                    if point.isdigit() and point != '0':
                        graph[start_char][point] = next_count
                    visited.add(next_position)
                    queue.append((next_count, next_position))


for point in get_initial_positions():
    bfs_update_graph(point)

zero_graph = graph.pop('0')
best = float('inf')
for perm in permutations(graph.keys()):
    total = zero_graph[perm[0]]
    for p in pairwise(perm):
        total += graph[p[0]][p[1]]
    total += zero_graph[perm[-1]]
    best = min(best, total)

print(best)
