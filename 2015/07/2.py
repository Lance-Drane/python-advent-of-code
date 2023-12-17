import re
import sys

circuits: dict[str, int] = {}
unresolved: dict[str, list[str]] = {}
circuits_initial: dict[str, int] = {}
unresolved_initial: dict[str, list[str]] = {}


def main_loop():
    while len(unresolved) > 0:
        to_remove = []
        for identifier, instruction in unresolved.items():
            if len(instruction) == 2 and instruction[1] in circuits:
                # NOT
                circuits[identifier] = 65535 - circuits[instruction[1]]
                to_remove.append(identifier)
            elif instruction[0] in circuits:
                if len(instruction) == 1:
                    circuits[identifier] = circuits[instruction[0]]
                    to_remove.append(identifier)
                elif instruction[1] == 'RSHIFT':
                    circuits[identifier] = circuits[instruction[0]] >> int(instruction[2])
                    to_remove.append(identifier)
                elif instruction[1] == 'LSHIFT':
                    circuits[identifier] = circuits[instruction[0]] << int(instruction[2])
                    to_remove.append(identifier)
                elif instruction[2] in circuits:
                    if instruction[1] == 'AND':
                        circuits[identifier] = circuits[instruction[0]] & circuits[instruction[2]]
                    else:
                        circuits[identifier] = circuits[instruction[0]] | circuits[instruction[2]]
                    to_remove.append(identifier)
                elif instruction[2].isdigit():
                    if instruction[1] == 'AND':
                        circuits[identifier] = circuits[instruction[0]] & int(instruction[2])
                    else:
                        circuits[identifier] = circuits[instruction[0]] | int(instruction[2])
                    to_remove.append(identifier)
            elif len(instruction) == 3 and instruction[2] in circuits and instruction[0].isdigit():
                circuits[identifier] = circuits[instruction[2]] & int(instruction[0])
                to_remove.append(identifier)

        for identifier in to_remove:
            del unresolved[identifier]


for line in sys.stdin.readlines():
    pattern = re.search(r'^(.*) -> (\w+)', line)
    instruction = pattern.group(1).split(' ')
    identifier = pattern.group(2)
    if len(instruction) == 1 and instruction[0].isdigit():
        circuits_initial[identifier] = int(instruction[0])
    else:
        unresolved_initial[identifier] = instruction

circuits = dict(circuits_initial)
unresolved = dict(unresolved_initial)
main_loop()
result = circuits['a']
circuits = dict(circuits_initial)
unresolved = dict(unresolved_initial)
circuits['b'] = result
main_loop()

print(circuits['a'])
