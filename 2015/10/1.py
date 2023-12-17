line = list(map(int, input()))

for _ in range(40):
    current = line[0]
    counter = 1
    local = []

    for char in line[1:]:
        if char == current:
            counter += 1
        else:
            local.append(counter)
            local.append(current)
            counter = 1
            current = char
    local.append(counter)
    local.append(current)
    line = local

print(len(line))
