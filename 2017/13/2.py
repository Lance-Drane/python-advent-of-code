import sys
from itertools import count

graph: dict[int, int] = {}
highest = -1
for line in sys.stdin.readlines():
    key, value = line.split(': ')
    key = int(key)
    graph[key] = (int(value) - 1) << 1
    highest = max(highest, key)

highest += 1
for starting_picosecond in count(start=0):
    caught = False
    for depth in range(highest):
        current_scanner = graph.get(depth)
        if current_scanner and (starting_picosecond + depth) % current_scanner == 0:
            caught = True
            break
    if not caught:
        print(starting_picosecond)
        break
