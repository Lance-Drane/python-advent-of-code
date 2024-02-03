LIST_SIZE = 256

nums = list(range(LIST_SIZE))
current_position = 0
lengths = list(map(int, input().split(',')))

for skip_size, length in enumerate(lengths):
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

print(nums[0] * nums[1])
