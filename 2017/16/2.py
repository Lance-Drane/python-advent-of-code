from itertools import count

base_programs = list('abcdefghijklmnop')
dances = input().split(',')


def dance(programs: list[str]) -> list[str]:
    def swap(x: int, y: int):
        tmp = programs[y]
        programs[y] = programs[x]
        programs[x] = tmp

    for dance in dances:
        move = dance[0]
        if move == 's':
            rotation = int(dance[1:])
            programs = programs[-rotation:] + programs[:-rotation]
        else:
            x, y = dance[1:].split('/')
            if move == 'x':
                x, y = int(x), int(y)
                swap(x, y)
            else:  # partner
                x, y = programs.index(x), programs.index(y)
                swap(x, y)

    return programs


programs = base_programs.copy()

# find cycle
for dance_iteration in count(start=1):  # noqa: B007 (we use the value later)
    programs = dance(programs)
    if programs == base_programs:
        break

# execute the cycle the appropriate number of times
for _ in range(1_000_000_000 % dance_iteration):
    programs = dance(programs)

print(''.join(programs))
