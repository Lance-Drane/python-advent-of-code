import sys


def subset_sum(numbers, target, partial, partial_sum):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1 :]
        yield from subset_sum(remaining, target, [*partial, n], partial_sum + n)


print(sum(1 for _ in subset_sum([int(line) for line in sys.stdin.readlines()], 150, [], 0)))
