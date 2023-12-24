import sys
from collections import defaultdict

bots: dict[str, list[int]] = defaultdict(list)


def parse_input():
    for line in sys.stdin.read().splitlines():
        parts = line.split(' ')
        if parts[0] == 'value':
            bots[parts[5]].append(int(parts[1]))
        else:
            yield parts


instructions = list(parse_input())

while True:
    for line in instructions:
        chips = bots[line[1]]
        if len(chips) < 2:
            continue
        low, high = (chips[0], chips[1]) if chips[0] < chips[1] else (chips[1], chips[0])
        if low == 17 and high == 61:
            print(line[1])
            sys.exit(0)
        low_dest, high_dest = line[5], line[10]
        if line[5] == 'bot':
            bots[line[6]].append(low)
        if line[10] == 'bot':
            bots[line[11]].append(high)
        chips.clear()
