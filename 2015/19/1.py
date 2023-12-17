import sys
from collections import defaultdict


def findall(pattern, string):
    idx = string.find(pattern)
    while idx != -1:
        yield idx
        idx = string.find(pattern, idx + 1)


graph = defaultdict(list)

lines = sys.stdin.readlines()
for line in lines[:-2]:
    start, _, end = line.rstrip().split(' ')
    graph[start].append(end)
string = lines[-1].rstrip()
combos = set()

for molecule, replacements in graph.items():
    for position in findall(molecule, string):
        end_position = len(molecule) + position
        for replace in replacements:
            combos.add(string[:position] + replace + string[end_position:])

print(len(combos))
