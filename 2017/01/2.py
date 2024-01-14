sequence = list(map(int, input()))
seq_1 = sequence[: len(sequence) // 2]
seq_2 = sequence[len(sequence) // 2 :]
total = 0
for left, right in zip(seq_1, seq_2, strict=False):
    if left == right:
        total += left << 1

print(total)
