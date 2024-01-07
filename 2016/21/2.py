import sys

scrambled = list('fbgdceah')


def swap(x: int, y: int):
    tmp = scrambled[y]
    scrambled[y] = scrambled[x]
    scrambled[x] = tmp


def rotate(x: int) -> list[str]:
    return scrambled[x:] + scrambled[:x]


instructions = sys.stdin.readlines()

for line in reversed(instructions):
    parts = line.split()
    if line[0] == 'm':  # move position
        x, y = int(parts[2]), int(parts[5])
        tmp = scrambled[y]
        scrambled.remove(tmp)
        scrambled.insert(x, tmp)
    elif line[1] == 'e':  # reverse
        x, y = int(parts[2]), int(parts[4]) + 1
        scrambled = scrambled[:x] + scrambled[x:y][::-1] + scrambled[y:]
    elif line[1] == 'o':  # rotate
        if line[7] == 'l':  # rotate left
            x = int(parts[2])
            scrambled = rotate(-x)
        elif line[7] == 'r':  # rotate right
            x = int(parts[2])
            scrambled = rotate(x)
        else:  # rotate based on position
            x = scrambled.index(parts[6])

            """
            re-rotation assumes that the list/string only has 8 characters
            other lengths do not necessarily have unique from -> to combinations

            here is the from -> to pattern from part 1, do this in reverse:
            0 -> 1
            1 -> 3
            2 -> 5
            3 -> 7
            4 -> 2
            5 -> 4
            6 -> 6
            7 -> 0
            """
            if x == 7:
                scrambled = rotate(4)
            elif x in (0, 1):
                scrambled = rotate(1)
            elif x == 2:
                scrambled = rotate(-2)
            elif x == 3:
                scrambled = rotate(2)
            elif x == 4:
                scrambled = rotate(-1)
            elif x == 5:
                scrambled = rotate(3)

    elif line[5] == 'l':  # swap letter
        x, y = scrambled.index(parts[2]), scrambled.index(parts[5])
        swap(x, y)
    else:  # swap position
        x, y = int(parts[2]), int(parts[5])
        swap(x, y)
    # print(scrambled)

print(''.join(scrambled))
