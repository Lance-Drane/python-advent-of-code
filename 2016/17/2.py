from collections import deque
from hashlib import md5


def is_open(char: str) -> bool:
    return char in ('b', 'c', 'd', 'e', 'f')


initial = input()
initial_len = len(initial)
queue = deque([(0, initial)])
best = ''

while queue:
    position, passcode = queue.popleft()
    passhash = md5(passcode.encode()).hexdigest()

    # right
    if position & 3 != 3 and is_open(passhash[3]):
        r_pass = f'{passcode}R'
        if position == 14:
            best = r_pass[initial_len:]
        else:
            queue.append((position + 1, r_pass))

    # down
    if position < 12 and is_open(passhash[1]):
        d_pass = f'{passcode}D'
        if position == 11:
            best = d_pass[initial_len:]
        else:
            queue.append((position + 4, d_pass))

    # left
    if position & 3 != 0 and is_open(passhash[2]):
        queue.append((position - 1, f'{passcode}L'))

    # top
    if position >= 4 and is_open(passhash[0]):
        queue.append((position - 4, f'{passcode}U'))

print(len(best))
