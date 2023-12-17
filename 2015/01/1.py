count = 0
for s in input():
    if s == '(':
        count += 1
    else:
        count -= 1

print(count)
