def flip_bits(binary_str: str):
    inverse = int(binary_str, 2) ^ (2 ** (len(binary_str) + 1) - 1)
    return bin(inverse)[3:]


TARGET_LENGTH = 272

data = input()
while len(data) < TARGET_LENGTH:
    data = f'{data}0{flip_bits(data[::-1])}'
data = data[:TARGET_LENGTH]

while len(data) & 1 != 1:
    # in python 3.12, can potentially use itertools.batched instead
    data = ['1' if chunk[0] == chunk[1] else '0' for chunk in zip(*[iter(data)] * 2, strict=False)]

print(''.join(data))
