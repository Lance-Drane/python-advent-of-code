import re
import sys


def window_iter(line):
    win = False
    for i in range(len(line) - 1):
        if line[i : i + 2] in ('ab', 'cd', 'pq', 'xy'):
            return False
        if line[i] == line[i + 1]:
            win = True
    return win


print(
    sum(
        1
        for _ in filter(
            lambda line: window_iter(line) and len(re.findall(r'[aeiou]', line)) >= 3, sys.stdin.readlines()
        )
    )
)
