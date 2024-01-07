from collections import deque

upper = int(input()) + 1
midpoint = upper // 2 + (upper & 1)

deque_1 = deque(range(1, midpoint))
deque_2 = deque(range(midpoint, upper))

while True:
    if len(deque_2) >= len(deque_1):
        deque_2.popleft()
        if not deque_2:
            print(deque_1[0])
            break
    else:
        deque_1.pop()
    deque_1.append(deque_2.popleft())
    deque_2.append(deque_1.popleft())
