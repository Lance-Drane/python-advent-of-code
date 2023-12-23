import re

groups = re.split(r'[^\w]+', input())
if groups[0] == '':
    groups = groups[1:]
stack: list[list[int, int]] = []
multiplier = 1

total = 0

for group in groups:
    if group[0].isdigit():
        fulllen = len(group) + 2
        for s in stack:
            s[0] -= fulllen
        next_subseq, next_repeat = map(int, group.split('x'))
        multiplier *= next_repeat
        stack.append([next_subseq, next_repeat])
    elif stack and len(group) > stack[0][0]:
        total += len(group[: stack[0][0]]) * multiplier
        total += len(group[stack[0][0] :])
        stack.clear()
        multiplier = 1
    else:
        total += len(group) * multiplier
        for s in stack:
            s[0] -= len(group)
        while stack and stack[-1][0] == 0:
            _, divisor = stack.pop()
            multiplier //= divisor

print(total)
