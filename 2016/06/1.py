import sys
from collections import Counter

data = sys.stdin.read().splitlines()
counters = [Counter() for _ in range(len(data[0]))]

for line in data:
    for idx, char in enumerate(line):
        counters[idx][char] += 1

print(''.join([counter.most_common(1)[0][0] for counter in counters]))
