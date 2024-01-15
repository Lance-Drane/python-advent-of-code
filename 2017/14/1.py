from functools import reduce

LIST_SIZE = 256

base = f'{input()}-'

used_squares = 0
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
    used_squares += sum(x.count('1') for x in bin_arr)

print(used_squares)
