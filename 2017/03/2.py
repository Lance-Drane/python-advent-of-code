from collections import defaultdict

target = int(input())
graph = defaultdict(lambda: 0, {(0, 0): 1})


def get_neighbors(point) -> int:
    x, y = point
    return sum(
        [
            graph[(x + 1, y)],
            graph[(x - 1, y)],
            graph[(x, y + 1)],
            graph[(x, y - 1)],
            graph[(x + 1, y - 1)],
            graph[(x + 1, y + 1)],
            graph[(x - 1, y - 1)],
            graph[(x - 1, y + 1)],
        ]
    )


curr = (1, 0)
edge_distance = 1
while True:
    next_sum = get_neighbors(curr)
    if next_sum > target:
        print(next_sum)
        break
    graph[curr] = next_sum

    # bottom left -> bottom right
    if curr[1] == edge_distance:
        curr = (curr[0] + 1, curr[1])
        if curr[0] > edge_distance:
            edge_distance += 1
    # top left -> bottom left
    elif curr[0] == -edge_distance:
        curr = (curr[0], curr[1] + 1)
    # top right -> top left
    elif curr[1] == -edge_distance:
        curr = (curr[0] - 1, curr[1])
    # bottom right -> top right
    else:
        curr = (curr[0], curr[1] - 1)
