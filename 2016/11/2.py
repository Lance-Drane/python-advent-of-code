import heapq
import re
import sys
from itertools import chain, combinations

# a lot of this solution, particularly the last floor heuristic, was taken from:
# https://www.reddit.com/r/adventofcode/comments/5hoia9/comment/db1zbu0/


def parse_input():
    elements_seen = {}
    read_state: list[list[int]] = [[] for _ in range(4)]
    for idx, line in enumerate(sys.stdin.readlines()):
        for item in re.finditer(r'[\w-]+ microchip|[\w-]+ generator', line):
            element, entity = item.group().split(' ')
            hyphen = element.find('-')
            refined = element if hyphen == -1 else element[:hyphen]
            num_rep = elements_seen.get(refined)
            if not num_rep:
                num_rep = len(elements_seen) + 1
                elements_seen[refined] = num_rep
            read_state[idx].append(num_rep if entity == 'generator' else -num_rep)
        read_state[idx] = tuple(sorted(read_state[idx]))
    return (0, tuple(read_state))


def no_explosion(floor):
    if not floor or floor[-1] < 0:  # no generators
        return True
    return all(-chip in floor for chip in floor if chip < 0)


initial = parse_input()
heap = []
heapq.heappush(heap, (0, initial))
state_costs = {initial: 0}

while heap:
    _, current = heapq.heappop(heap)
    floor, items = current
    if floor == 3 and not any(len(f) for f in items[:-1]):
        break

    directions = [direc for direc in (-1, 1) if 0 <= floor + direc < 4]
    # with 2-length combinations: don't move incompatible pairs
    for move in chain(
        combinations(items[floor], 1),
        filter(lambda c: abs(c[0]) == abs(c[1]) or c[0] * c[1] > 0, combinations(items[floor], 2)),
    ):
        for direction in directions:
            # do not go down if there is no item below where we are
            if direction == -1 and not any(len(f) for f in items[:floor]):
                continue
            new_floors = list(items)
            new_floors[floor] = tuple(x for x in items[floor] if x not in move)
            new_floors[floor + direction] = tuple(sorted(items[floor + direction] + move))

            if not no_explosion(new_floors[floor]) or not no_explosion(new_floors[floor + direction]):
                continue

            next_state = (floor + direction, tuple(new_floors))
            new_cost = state_costs[current] + 1
            if next_state not in state_costs or new_cost < state_costs[next_state]:
                state_costs[next_state] = new_cost
                # prioritize adding items to floor 4
                priority = new_cost - len(new_floors[3]) * 10
                heapq.heappush(heap, (priority, next_state))

# we don't need to manage the input for the new items. We add two complete pairs on the first floor.
# It will ALWAYS take 12 moves minimum to move a complete pair from floor 1 to floor 4
# so just add 24 to the sum from part 1
print(state_costs[current] + 24)
