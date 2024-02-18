import sys

ITERATIONS = 18

rules: dict[tuple[str], tuple[str]] = {}
for line in sys.stdin.readlines():
    start, _, end = line.split()
    rules[tuple(start.split('/'))] = tuple(end.split('/'))


def get_transformations(graph: tuple[str, ...]):
    yield graph
    yield tuple(reversed(graph))

    t = tuple(''.join(reversed(a)) for a in graph)[::-1]  # rotate 180 degrees
    yield t
    yield tuple(reversed(t))

    t = tuple(''.join(a) for a in zip(*graph, strict=False))[::-1]  # rotate 90 degrees counter-clockwise
    yield t
    yield tuple(reversed(t))

    t = tuple(''.join(reversed(a)) for a in zip(*graph, strict=False))  # rotate 90 degrees clockwise
    yield t
    yield tuple(reversed(t))


def rebuild_graph(graph: list[str]):
    length = len(graph)
    chunk_size = 2 if length & 1 == 0 else 3
    new_graph = []
    for y in range(0, length, chunk_size):
        row_chunks = []
        for x in range(0, length, chunk_size):
            chunk = tuple(graph[y2][x : x + chunk_size] for y2 in range(y, y + chunk_size))
            new_chunk = None
            for key in get_transformations(chunk):
                potential = rules.get(key)
                if potential:
                    new_chunk = potential
                    break
            row_chunks.append(new_chunk)

        for i in range(len(row_chunks[0])):
            base = ''
            for part in row_chunks:
                base += part[i]
            new_graph.append(base)

    return new_graph


graph = ['.#.', '..#', '###']

for _ in range(ITERATIONS):
    graph = rebuild_graph(graph)

print(sum(row.count('#') for row in graph))
