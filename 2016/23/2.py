import sys
from collections import defaultdict

registers = defaultdict(int, {'a': 12})

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
            amount = registers[instruct[2]] if instruct[2][0].isalpha() else int(instruct[2])
            # you'll want to optimize for multiplication based on the amount from here
            if amount == -2:
                if (
                    instructions[curr - 2][0] == 'inc'
                    and instructions[curr - 1][0] == 'dec'
                    and instruct[1] == instructions[curr - 1][1]
                ):
                    registers[instructions[curr - 2][1]] += jnz_check
                    registers[instruct[1]] = 0
                    curr += 1
                elif (
                    instructions[curr - 2][0] == 'dec'
                    and instructions[curr - 1][0] == 'inc'
                    and instruct[1] == instructions[curr - 2][1]
                ):
                    registers[instructions[curr - 1][1]] += jnz_check
                    registers[instruct[1]] = 0
                    curr += 1
                else:
                    curr += amount
            elif amount == -5:
                # this is the main optimization to be done
                last_5_instructions = [instructions[i] for i in range(curr - 5, curr)]
                if last_5_instructions[0][0] == 'cpy':
                    product = (
                        registers[last_5_instructions[0][1]]
                        if last_5_instructions[0][1][0].isalpha()
                        else int(last_5_instructions[0][1])
                    )
                    # in my input, register 'a' was always the one incremented here, YMMV

                    registers['a'] += jnz_check * product
                    registers[instruct[1]] = 0
                    curr += 1
                else:
                    curr += amount
            else:
                curr += amount
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
