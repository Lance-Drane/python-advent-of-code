from functools import reduce

LIST_SIZE = 256

base = f'{input()}-'

grid = []
for row in range(128):
    nums = list(range(LIST_SIZE))
    current_position = 0
    skip_size = 0
    lengths = [ord(x) for x in f'{base}{row}'] + [17, 31, 73, 47, 23]
    for _ in range(64):
        for length in lengths:
            forward = current_position + length
            if forward > LIST_SIZE:
                last_idx = forward % LIST_SIZE
                sublist = nums[current_position:] + nums[:last_idx]
                sublist = sublist[::-1]
                sublist_breakpoint = (len(sublist) - last_idx) % len(sublist)
                nums = sublist[sublist_breakpoint:] + nums[last_idx:current_position] + sublist[:sublist_breakpoint]
            else:
                nums = nums[:current_position] + nums[current_position:forward][::-1] + nums[forward:]
            current_position = (forward + skip_size) % LIST_SIZE
            skip_size += 1

    bin_arr = [format(reduce(lambda x, y: x ^ y, nums[idx : idx + 16]), 'b').zfill(8) for idx in range(0, 256, 16)]
    grid.append(list(''.join(bin_arr)))

groups = 0
for y in range(128):
    for x in range(128):
        if grid[y][x] == '0':
            continue
        grid[y][x] = '0'
        stack = [(y, x)]
        while stack:
            curr_y, curr_x = stack.pop()
            # top
            if curr_y > 0 and grid[curr_y - 1][curr_x] == '1':
                grid[curr_y - 1][curr_x] = '0'
                stack.append((curr_y - 1, curr_x))
            # right
            if curr_x < 127 and grid[curr_y][curr_x + 1] == '1':
                grid[curr_y][curr_x + 1] = '0'
                stack.append((curr_y, curr_x + 1))
            # bottom
            if curr_y < 127 and grid[curr_y + 1][curr_x] == '1':
                grid[curr_y + 1][curr_x] = '0'
                stack.append((curr_y + 1, curr_x))
            # left
            if curr_x > 0 and grid[curr_y][curr_x - 1] == '1':
                grid[curr_y][curr_x - 1] = '0'
                stack.append((curr_y, curr_x - 1))

        groups += 1

print(groups)
