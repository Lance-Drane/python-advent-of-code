import sys
from collections import defaultdict

bots: dict[str, list[int]] = defaultdict(list)
outputs: dict[str, int] = {}


def parse_input():
    for line in sys.stdin.read().splitlines():
        parts = line.split(' ')
        if parts[0] == 'value':
            bots[parts[5]].append(int(parts[1]))
        else:
            yield parts


instructions = list(parse_input())

while any(a for a in bots.values()):
    for line in instructions:
        chips = bots[line[1]]
        if len(chips) < 2:
            continue
        low, high = (chips[0], chips[1]) if chips[0] < chips[1] else (chips[1], chips[0])
        if line[5] == 'bot':
            bots[line[6]].append(low)
        else:
            outputs[line[6]] = low
        if line[10] == 'bot':
            bots[line[11]].append(high)
        else:
            outputs[line[11]] = high
        chips.clear()

print(outputs['0'] * outputs['1'] * outputs['2'])
