import re
import sys
from itertools import count, cycle, islice


def get_target_position(num_positions: int, idx: int) -> int:
    target_position = num_positions - idx - 1
    while target_position < 0:
        target_position += num_positions
    return target_position


# first value = target position, second value = the infinite cycle
cycles = [
    (get_target_position(int(c[1]), idx), islice(cycle(range(int(c[1]))), int(c[3]), None))
    for idx, c in enumerate([re.findall(r'[\d]+', line) for line in sys.stdin.readlines()])
]

for time in count():
    valid = True
    for disc in cycles:
        cont = next(disc[1])
        if cont != disc[0]:
            valid = False
    if valid:
        print(time)
        break
