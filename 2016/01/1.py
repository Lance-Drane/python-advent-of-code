vertical = 0
horizontal = 0
dirs = ('U', 'R', 'D', 'L')
curr_dir_idx = 0

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
        vertical -= amount
    elif curr_dir == 'R':
        horizontal += amount
    elif curr_dir == 'D':
        vertical += amount
    else:
        horizontal -= amount

print(abs(vertical) + abs(horizontal))
