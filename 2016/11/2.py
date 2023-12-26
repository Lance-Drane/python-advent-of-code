import re
import sys
from collections import deque
from copy import deepcopy
from itertools import chain, combinations


def parse_input():
    read_state = [set() for _ in range(4)]
    for idx, line in enumerate(sys.stdin.readlines()):
        for item in re.finditer(r'[\w-]+ microchip|[\w-]+ generator', line):
            element, entity = item.group().split(' ')
            hyphen = element.find('-')
            refined = element if hyphen == -1 else element[:hyphen]
            read_state[idx].add((refined, entity))
    return read_state


def get_state_hash(elevator, state):
    state_hash = sorted(item for sublist in state for item in sublist)
    for floor, sublist in enumerate(state):
        for item in sublist:
            state_hash[state_hash.index(item)] = floor
    return (elevator, tuple(state_hash))


def get_next_state(elevator: int, state: list[set[tuple[str, str]]]):
    # with 2-length combinations: don't move incompatible pairs
    for combo in chain(
        combinations(state[elevator], 1),
        filter(lambda c: c[0][0] == c[1][0] or c[0][1] == c[1][1], combinations(state[elevator], 2)),
    ):
        for new_elevator in (elevator - 1, elevator + 1):
            if new_elevator < 0 or new_elevator > 3:
                continue
            # do not go down if there is no item below where we are
            if new_elevator < elevator and not any(len(state[idx]) for idx in range(elevator)):
                continue
            new_state = deepcopy(state)
            for item in combo:
                new_state[elevator].remove(item)
                new_state[new_elevator].add(item)
            # validate no explosion on both last floor and next floor
            safe = True
            for floor in elevator, new_elevator:
                generators = {sta for sta in new_state[floor] if sta[1] == 'generator'}
                if generators and any(
                    sta[1] != 'generator' and (sta[0], 'generator') not in generators for sta in new_state[floor]
                ):
                    safe = False
                    break
            if safe:
                yield new_elevator, new_state


# TODO make me faster!
initial_state = parse_input()
queue: deque[tuple[int, int, list[set[tuple[str, str]]]]] = deque([(0, 0, initial_state)])
visited = {get_state_hash(0, initial_state)}
while queue:
    moves, elevator, state = queue.popleft()
    # success
    if len(state[3]) and not any(len(state[idx]) for idx in range(3)):
        # we don't need to manage the input for the new items. We add two complete pairs on the first floor.
        # It will ALWAYS take 12 moves minimum to move a complete pair from floor 1 to floor 4
        # so just add 24 to the sum from part 1
        print(moves + 24)
        break

    for new_elevator, new_state in get_next_state(elevator, state):
        new_hash = get_state_hash(new_elevator, new_state)
        if new_hash in visited:
            continue
        visited.add(new_hash)
        # print(new_hash)
        queue.append((moves + 1, new_elevator, new_state))
