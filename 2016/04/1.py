import sys
from collections import Counter

total = 0
for line in sys.stdin.readlines():
    parts = line.split('-')
    if line.rstrip()[-6:-1] == ''.join(p[0] for p in Counter(sorted(''.join(parts[:-1]))).most_common(5)):
        total += int(parts[-1][: parts[-1].find('[')])

print(total)
