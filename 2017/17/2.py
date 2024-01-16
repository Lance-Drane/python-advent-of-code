REPEAT_TIMES = 50_000_000
num_steps = int(input())

curr_pos = 0
first_pos = 0
for i in range(1, REPEAT_TIMES + 1):
    curr_pos = (curr_pos + num_steps) % i + 1
    if curr_pos == 1:
        first_pos = i
print(first_pos)
