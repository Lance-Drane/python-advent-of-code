import re
import sys


def has_abba(string):
    return any(
        string[i] != string[i + 1] and string[i] == string[i + 3] and string[i + 1] == string[i + 2]
        for i in range(len(string) - 3)
    )


count = 0
for line in sys.stdin.readlines():
    parts = re.split(r'[\[\]]', line.rstrip())
    if any(has_abba(s) for s in parts[::2]) and not any(has_abba(s) for s in parts[1::2]):
        count += 1
print(count)
