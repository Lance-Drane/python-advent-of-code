import sys

TARGET = 150


def subset_sum(numbers, partial, partial_sum):
    if partial_sum == TARGET:
        yield partial
    if partial_sum >= TARGET:
        return
    for i, n in enumerate(numbers):
        yield from subset_sum(numbers[i + 1 :], [*partial, n], partial_sum + n)


print(sum(1 for _ in subset_sum([int(line) for line in sys.stdin.readlines()], [], 0)))
