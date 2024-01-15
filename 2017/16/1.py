programs = list('abcdefghijklmnop')


def swap(x: int, y: int):
    tmp = programs[y]
    programs[y] = programs[x]
    programs[x] = tmp


for dance in input().split(','):
    move = dance[0]
    if move == 's':
        rotation = int(dance[1:])
        programs = programs[-rotation:] + programs[:-rotation]
    else:
        x, y = dance[1:].split('/')
        if move == 'x':
            x, y = int(x), int(y)
        else:  # partner
            x, y = programs.index(x), programs.index(y)
        swap(x, y)

print(''.join(programs))
