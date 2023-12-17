line = input()
pos = (0, 0)
visited = {(0, 0)}


def compute_new_position(char, position):
    if char == '^':
        return (position[0] + 1, position[1])
    if char == '>':
        return (position[0], position[1] + 1)
    if char == 'v':
        return (position[0] - 1, position[1])
    return (position[0], position[1] - 1)


for i in range(0, len(line), 2):
    pos = compute_new_position(line[i], pos)
    visited.add(pos)
pos = (0, 0)
for i in range(1, len(line), 2):
    pos = compute_new_position(line[i], pos)
    visited.add(pos)

print(len(visited))
