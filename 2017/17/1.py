REPEAT_TIMES = 2017

num_steps = int(input())
buffer = [0]
curr_pos = 0

for i in range(1, REPEAT_TIMES + 1, 1):
    curr_pos = (curr_pos + num_steps) % i + 1
    buffer.insert(curr_pos, i)

print(buffer[curr_pos + 1])
