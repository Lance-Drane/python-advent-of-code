from itertools import pairwise

sequence = list(map(int, input()))
total = 0
for left, right in pairwise(sequence):
    if left == right:
        total += left

if len(sequence) > 2 and sequence[0] == sequence[-1]:
    total += sequence[0]

print(total)
