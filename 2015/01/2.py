count = 0
for idx, s in enumerate(input()):
    if s == '(':
        count += 1
    else:
        count -= 1
        if count == -1:
            print(idx + 1)
            break
