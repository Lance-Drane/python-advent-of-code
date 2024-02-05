import sys
from collections import defaultdict

registers = defaultdict(int)
instructions: list[list[str, str, str]] = [line.split() for line in sys.stdin.readlines()]
last_sound = 0


def get_next_value(val: str) -> int:
    return int(val) if not val[0].isalpha() else registers[val]


curr = 0
while curr < len(instructions):
    instruct = instructions[curr]

    if instruct[0] == 'snd':
        last_sound = get_next_value(instruct[1])
        curr += 1
    elif instruct[0] == 'set':
        registers[instruct[1]] = get_next_value(instruct[2])
        curr += 1
    elif instruct[0] == 'add':
        registers[instruct[1]] += get_next_value(instruct[2])
        curr += 1
    elif instruct[0] == 'mul':
        registers[instruct[1]] *= get_next_value(instruct[2])
        curr += 1
    elif instruct[0] == 'mod':
        registers[instruct[1]] %= get_next_value(instruct[2])
        curr += 1
    elif instruct[0] == 'rcv':
        next_val = get_next_value(instruct[1])
        if next_val != 0:
            print(last_sound)
            break
        curr += 1
    # jgz
    elif get_next_value(instruct[1]) > 0:
        curr += get_next_value(instruct[2])
    else:
        curr += 1
