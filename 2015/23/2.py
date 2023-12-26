import re
import sys

registers = {
    'a': 1,
    'b': 0,
}

instructions = tuple(tuple(a.group() for a in re.finditer(r'[\w-]+', line)) for line in sys.stdin.readlines())
curr = 0

while curr < len(instructions) and curr >= 0:
    instruct = instructions[curr]

    if instruct[0] == 'hlf':
        registers[instruct[1]] >>= 1
        curr += 1
    elif instruct[0] == 'tpl':
        registers[instruct[1]] *= 3
        curr += 1
    elif instruct[0] == 'inc':
        registers[instruct[1]] += 1
        curr += 1
    elif instruct[0] == 'jmp':
        curr += int(instruct[1])
    elif instruct[0] == 'jie':
        if registers[instruct[1]] & 1 == 0:
            curr += int(instruct[2])
        else:
            curr += 1
    elif registers[instruct[1]] == 1:
        curr += int(instruct[2])
    else:
        curr += 1

print(registers['b'])
