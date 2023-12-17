import sys


def double_pair(line):
    visited = set()
    prev = ''
    for i in range(len(line) - 1):
        chunk = line[i : i + 2]
        if chunk != prev and chunk in visited:
            return True
        visited.add(chunk)
        prev = chunk
    return False


print(
    sum(
        1
        for _ in filter(
            lambda line: any(line[i] == line[i + 2] for i in range(len(line) - 2)) and double_pair(line),
            sys.stdin.readlines(),
        )
    )
)
