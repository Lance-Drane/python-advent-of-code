import sys

password = list('abcdefgh')


def swap(x: int, y: int):
    tmp = password[y]
    password[y] = password[x]
    password[x] = tmp


def rotate(x: int) -> list[str]:
    return password[x:] + password[:x]


for line in sys.stdin.readlines():
    parts = line.split()
    if line[0] == 'm':  # move position
        x, y = int(parts[2]), int(parts[5])
        tmp = password[x]
        password.remove(tmp)
        password.insert(y, tmp)
    elif line[1] == 'e':  # reverse
        x, y = int(parts[2]), int(parts[4]) + 1
        password = password[:x] + password[x:y][::-1] + password[y:]
    elif line[1] == 'o':  # rotate
        if line[7] == 'l':  # rotate left
            x = int(parts[2])
            password = rotate(x)
        elif line[7] == 'r':  # rotate right
            x = int(parts[2])
            password = rotate(-x)
        else:  # rotate based on position
            x = password.index(parts[6])
            password = rotate(-x)
            password = rotate(-2) if x >= 4 else rotate(-1)
    elif line[5] == 'l':  # swap letter
        x, y = password.index(parts[2]), password.index(parts[5])
        swap(x, y)
    else:  # swap position
        x, y = int(parts[2]), int(parts[5])
        swap(x, y)

print(''.join(password))
