import sys
from collections import defaultdict
from itertools import count

base_instructions: list[list[str, str, str]] = [line.split() for line in sys.stdin.readlines()]
curr = 0

try:
    for init in count(start=1):
        registers = defaultdict(int, {'a': init})
        curr = 0
        instructions = base_instructions.copy()
        out = []
        next_value = 0
        while curr < len(instructions):
            instruct = instructions[curr]
            # print(init, instruct, dict(registers), file=sys.stderr)

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
                            registers[instructions[curr - 2][1]] += jnz_check + 1
                            registers[instruct[1]] = 0
                            curr += 1
                        elif (
                            instructions[curr - 2][0] == 'dec'
                            and instructions[curr - 1][0] == 'inc'
                            and instruct[1] == instructions[curr - 2][1]
                        ):
                            registers[instructions[curr - 1][1]] += jnz_check + 1
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
                            for i in last_5_instructions[1:]:
                                if i[0] == 'inc':
                                    register_key = i[1]
                                    break
                            registers[register_key] += jnz_check * product - 1
                            registers[instruct[1]] = 0
                            curr += 1
                        else:
                            curr += amount
                    else:
                        curr += amount
                else:
                    curr += 1
            else:  # 'out'
                trans_value = registers[instruct[1]] if instruct[1][0].isalpha() else int(instruct[1])
                if trans_value != next_value:
                    break
                next_value = 0 if next_value == 1 else 1
                out.append(trans_value)
                if len(out) == 100:
                    print(init)
                    sys.exit(0)
                curr += 1
except KeyboardInterrupt:
    print(init)
