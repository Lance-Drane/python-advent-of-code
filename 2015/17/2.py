import sys


def subset_sum(numbers, target, partial, partial_sum):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1 :]
        yield from subset_sum(remaining, target, [*partial, n], partial_sum + n)


count = 0
smallest = float('inf')

for size in map(len, subset_sum([int(line) for line in sys.stdin.readlines()], 150, [], 0)):
    if size < smallest:
        smallest = size
        count = 1
    elif size == smallest:
        count += 1

print(count)
