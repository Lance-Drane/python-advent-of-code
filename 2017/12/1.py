import re
import sys

graph = {}

for line in sys.stdin.readlines():
    nums = re.findall(r'[\d]+', line)
    graph[nums[0]] = nums[1:]

visited = {'0'}


def dfs(key: str):
    for connection in graph[key]:
        if connection in visited:
            continue
        visited.add(connection)
        dfs(connection)


dfs('0')

print(len(visited))
