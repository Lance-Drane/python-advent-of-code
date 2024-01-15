import sys

A_FACTOR = 16807
B_FACTOR = 48271
REMAINDER = 2147483647

stdin = sys.stdin.readlines()
a_value = int(stdin[0].split()[-1])
b_value = int(stdin[1].split()[-1])

count = 0
for _ in range(40_000_000):
    a_value = a_value * A_FACTOR % REMAINDER
    b_value = b_value * B_FACTOR % REMAINDER
    a_bin = format(a_value, 'b').zfill(16)[-16:]
    b_bin = format(b_value, 'b').zfill(16)[-16:]
    if a_bin == b_bin:
        count += 1

print(count)
