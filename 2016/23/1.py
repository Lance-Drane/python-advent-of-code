import sys
from collections import defaultdict

registers = defaultdict(int, {'a': 7})

instructions: list[list[str, str, str]] = [line.split() for line in sys.stdin.readlines()]
curr = 0

while curr < len(instructions):
    instruct = instructions[curr]

    if instruct[0] == 'cpy':
        if instruct[2][0].isalpha():
            registers[instruct[2]] = registers[instruct[1]] if instruct[1][0].isalpha() else int(instruct[1])
        curr += 1
    elif instruct[0] == 'inc':
        if instruct[1][0].isalpha():
            registers[instruct[1]] += 1
        curr += 1
    elif instruct[0] == 'dec':
        if instruct[1][0].isalpha():
            registers[instruct[1]] -= 1
        curr += 1
    elif instruct[0] == 'jnz':
        jnz_check = registers[instruct[1]] if instruct[1][0].isalpha() else int(instruct[1])
        if jnz_check != 0:
            curr += registers[instruct[2]] if instruct[2][0].isalpha() else int(instruct[2])
        else:
            curr += 1
    else:  # 'tgl'
        away = curr + (registers[instruct[1]] if instruct[1][0].isalpha() else int(instruct[1]))
        if away < len(instructions):
            instruct_to_modify = instructions[away]
            if len(instruct_to_modify) == 2:
                if instruct_to_modify[0] == 'inc':
                    instruct_to_modify[0] = 'dec'
                else:
                    instruct_to_modify[0] = 'inc'
            elif instruct_to_modify[0] == 'jnz':
                instruct_to_modify[0] = 'cpy'
            else:
                instruct_to_modify[0] = 'jnz'
            instructions[away] = instruct_to_modify
        curr += 1

print(registers['a'])
