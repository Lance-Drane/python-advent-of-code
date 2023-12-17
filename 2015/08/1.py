import sys

total = 0

for line in sys.stdin.readlines():
    escaped = 2

    i = 1
    while i < len(line) - 1:
        if line[i] == '\\':
            if line[i + 1] == 'x':
                i += 4
                escaped += 3
            else:
                i += 2
                escaped += 1
        else:
            i += 1
    total += escaped

print(total)
