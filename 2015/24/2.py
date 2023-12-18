import sys
from itertools import combinations
from math import prod

presents = [int(line) for line in sys.stdin.readlines()]
target = sum(presents) >> 2

combo_length = 1
combos = None
while not combos:
    combos = list(filter(lambda c: sum(c) == target, combinations(presents, combo_length)))
    combo_length += 1

print(min(prod(combo) for combo in combos))
