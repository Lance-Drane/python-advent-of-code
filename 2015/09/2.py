import sys
from collections import defaultdict
from itertools import pairwise, permutations

graph = defaultdict(dict)

for line in sys.stdin.readlines():
    chunk = line.split(' ')
    weight, one, two = int(chunk[4]), chunk[0], chunk[2]
    graph[one][two] = weight
    graph[two][one] = weight

print(max(sum(graph[p[0]][p[1]] for p in pairwise(perm)) for perm in permutations(graph.keys())))
