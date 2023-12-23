data = input()
pointer = 0
total = 0

while True:
    # pre-marker text
    while pointer < len(data) and data[pointer] != '(':
        pointer += 1
        total += 1
    if pointer == len(data):
        break
    pointer += 1

    # parse subsequent
    l_pointer = pointer
    while data[pointer] != 'x':
        pointer += 1
    subsequent = int(''.join(data[l_pointer:pointer]))
    pointer += 1

    # parse repeat
    l_pointer = pointer
    while data[pointer] != ')':
        pointer += 1
    repeat = int(''.join(data[l_pointer:pointer]))
    pointer += 1

    # decompress marker
    l_pointer = pointer
    pointer += subsequent
    total += subsequent * repeat

print(total)
