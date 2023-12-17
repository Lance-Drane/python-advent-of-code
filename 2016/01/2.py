import sys

position = (0, 0)
visited = {(0, 0)}
dirs = ('U', 'R', 'D', 'L')
curr_dir_idx = 0


def handle_position():
    if position in visited:
        print(abs(position[0]) + abs(position[1]))
        sys.exit(0)
    visited.add(position)


for turn, amount in ((coord[0], int(coord[1:])) for coord in input().split(', ')):
    if turn == 'R':
        if curr_dir_idx == 3:
            curr_dir_idx = 0
        else:
            curr_dir_idx += 1
    elif curr_dir_idx == 0:
        curr_dir_idx = 3
    else:
        curr_dir_idx -= 1
    curr_dir = dirs[curr_dir_idx]

    if curr_dir == 'U':
        for i in reversed(range(position[0] - amount, position[0])):
            position = (i, position[1])
            handle_position()
    elif curr_dir == 'R':
        for i in range(position[1] + 1, position[1] + 1 + amount):
            position = (position[0], i)
            handle_position()
    elif curr_dir == 'D':
        for i in range(position[0] + 1, position[0] + 1 + amount):
            position = (i, position[1])
            handle_position()
    else:
        for i in reversed(range(position[1] - amount, position[1])):
            position = (position[0], i)
            handle_position()
