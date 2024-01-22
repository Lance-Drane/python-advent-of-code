from collections import defaultdict
from itertools import cycle, islice

banks = list(map(int, input().split()))
divisor = len(banks) - 1

seen = defaultdict(int, {tuple(banks): 1})
counter = 0

while True:
    max_idx, max_val = max(enumerate(banks), key=lambda x: x[1])
    decrement_by = max_val // divisor if max_val > divisor else divisor // max_val

    iterable = islice(cycle(range(len(banks))), max_idx + 1, None)
    curr_idx = next(iterable)
    while curr_idx != max_idx:
        next_val = max(0, max_val - decrement_by)
        banks[curr_idx] += max_val - next_val
        max_val = next_val
        curr_idx = next(iterable)
    banks[max_idx] = max_val
    next_seen = tuple(banks)
    seen[next_seen] += 1
    if seen[next_seen] == 2:
        counter += 1
    elif seen[next_seen] == 3:
        break

print(counter)
