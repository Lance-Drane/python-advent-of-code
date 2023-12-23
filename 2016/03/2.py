import sys
from itertools import islice

count = 0
chunks = map(int, sys.stdin.read().split())

while chunk := list(islice(chunks, 9)):
    for i in range(3):
        parts = sorted([chunk[i], chunk[i + 3], chunk[i + 6]])
        if parts[0] + parts[1] > parts[2]:
            count += 1

print(count)
