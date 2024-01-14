import sys

target = int(input())

if target == 1:
    print(0)
    sys.exit(0)

side_length = 1
min_steps = 0
while side_length**2 < target:
    side_length += 2
    min_steps += 1
mod_target = min_steps + 1
mod_amount = min_steps << 1
mod_diff = target % mod_amount
if mod_diff == 0:
    mod_diff = mod_amount

print(min_steps + abs(mod_target - mod_diff))
