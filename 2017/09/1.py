stream = input()
pointer = 0
next_score = 0
total_score = 0
garbage = False

while pointer < len(stream):
    char = stream[pointer]
    if char == '<':
        garbage = True
    elif garbage:
        if char == '!':
            pointer += 2
            continue
        if char == '>':
            garbage = False
    elif char == '{':
        next_score += 1
    elif char == '}':
        total_score += next_score
        next_score = max(0, next_score - 1)

    pointer += 1

print(total_score)
