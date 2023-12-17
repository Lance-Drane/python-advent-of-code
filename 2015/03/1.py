position = (0, 0)
visited = {(0, 0)}

for char in input():
    if char == '^':
        position = (position[0] + 1, position[1])
    elif char == '>':
        position = (position[0], position[1] + 1)
    elif char == 'v':
        position = (position[0] - 1, position[1])
    else:
        position = (position[0], position[1] - 1)
    visited.add(position)

print(len(visited))
