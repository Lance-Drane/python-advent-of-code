import sys

A_FACTOR = 16807
B_FACTOR = 48271
REMAINDER = 2147483647

stdin = sys.stdin.readlines()
a_value = int(stdin[0].split()[-1])
b_value = int(stdin[1].split()[-1])

count = 0
for _ in range(5_000_000):
    a_value = a_value * A_FACTOR % REMAINDER
    while a_value & 3 != 0:
        a_value = a_value * A_FACTOR % REMAINDER

    b_value = b_value * B_FACTOR % REMAINDER
    while b_value & 7 != 0:
        b_value = b_value * B_FACTOR % REMAINDER

    if a_value & 65535 == b_value & 65535:
        count += 1

print(count)
