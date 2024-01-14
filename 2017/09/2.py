stream = input()
pointer = 0
total_garbage = 0
garbage = False

while pointer < len(stream):
    char = stream[pointer]

    if garbage:
        if char == '!':
            pointer += 2
            continue
        if char == '>':
            garbage = False
        else:
            total_garbage += 1
    elif char == '<':
        garbage = True

    pointer += 1

print(total_garbage)
