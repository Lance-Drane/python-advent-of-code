import re
import sys

graph = {}

for line in sys.stdin.readlines():
    nums = re.findall(r'[\d]+', line)
    graph[nums[0]] = nums[1:]

visited = set()


def dfs(key: str):
    for connection in graph[key]:
        if connection in visited:
            continue
        visited.add(connection)
        dfs(connection)


counter = 0
for program in graph:
    if program in visited:
        continue
    visited.add(program)
    dfs(program)
    counter += 1

print(counter)
