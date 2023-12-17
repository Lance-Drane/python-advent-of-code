line = list(input())


# this mutates the global line variable
def increment():
    # detect no-no letters and immediately remove them (letters after them get defaulted to 'a')
    for idx, char in enumerate(line):
        if char in ['i', 'o', 'l']:
            line[idx] = chr(ord(char) + 1)
            for nidx in range(idx + 1, 8):
                line[nidx] = 'a'
            return

    # normal increment
    for idx, char in enumerate(reversed(line)):
        if char == 'z':
            line[-(idx + 1)] = 'a'
        else:
            line[-(idx + 1)] = chr(ord(char) + 1)
            return


# no-no letters get checked in increment
def valid():
    pairs = 0
    idx = 0
    while idx < 7:
        if line[idx] == line[idx + 1]:
            pairs += 1
            idx += 2
        else:
            idx += 1
    if pairs < 2:
        return False

    # sequence
    return any(ord(line[i + 1]) - ord(line[i]) == 1 and ord(line[i + 2]) - ord(line[i]) == 2 for i in range(6))


increment()
while not valid():
    increment()

print(''.join(line))
