import sys

graph = {}

lines = sys.stdin.readlines()
for line in lines[:-2]:
    start, _, end = line.rstrip().split(' ')
    graph[end] = start
string = lines[-1].rstrip()

graph = sorted(graph.items(), reverse=True, key=lambda i: len(i[0]))
count = 0

while string != 'e':
    for end, start in graph:
        count += string.count(end)
        string = string.replace(end, start)

print(count)
