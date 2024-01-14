import sys

instructions = list(map(int, sys.stdin.read().split()))
position = 0
steps = 0

while position >= 0 and position < len(instructions):
    steps += 1
    jump = instructions[position]
    instructions[position] += 1
    position += jump

print(steps)
