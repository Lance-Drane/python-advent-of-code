import sys

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0,
}

instructions: list[list[str, str, str]] = [line.split() for line in sys.stdin.readlines()]
curr = 0

while curr < len(instructions):
    instruct = instructions[curr]

    if instruct[0] == 'cpy':
        registers[instruct[2]] = registers[instruct[1]] if instruct[1][0].isalpha() else int(instruct[1])
        curr += 1
    elif instruct[0] == 'inc':
        registers[instruct[1]] += 1
        curr += 1
    elif instruct[0] == 'dec':
        registers[instruct[1]] -= 1
        curr += 1
    elif instruct[1][0].isdigit() or registers[instruct[1]] != 0:
        curr += int(instruct[2])
    else:
        curr += 1

print(registers['a'])
