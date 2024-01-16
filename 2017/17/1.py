from itertools import cycle, islice

REPEAT_TIMES = 2017

num_steps = int(input())
buffer = [0]
start_position = 0

for i in range(1, REPEAT_TIMES + 1, 1):
    iterator = islice(cycle(range(len(buffer))), start_position, None)
    for _ in range(num_steps):
        next(iterator)
    new_idx = next(iterator) + 1
    buffer.insert(new_idx, i)
    start_position = new_idx

print(buffer[start_position + 1])
