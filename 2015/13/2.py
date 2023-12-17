import sys
from collections import defaultdict
from itertools import permutations

# "!" = the lowest printable ASCII character other than " "
graph: dict[str, dict[str, int]] = defaultdict(dict, {'!': {}})

for line in sys.stdin.readlines():
    chunk = line.rstrip('\n').split(' ')
    graph[chunk[0]][chunk[10].rstrip('.')] = int(chunk[3]) if chunk[2] == 'gain' else -int(chunk[3])

for key in list(graph.keys())[1:]:
    graph['!'][key] = 0
    graph[key]['!'] = 0

print(
    max(
        sum(graph[perm[i]][perm[i + 1]] + graph[perm[i + 1]][perm[i]] for i in range(-1, len(graph) - 1))
        for perm in permutations(graph.keys())
    )
)
