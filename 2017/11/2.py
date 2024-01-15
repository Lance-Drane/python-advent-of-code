backtrack_map = {
    'n': 's',
    's': 'n',
    'nw': 'se',
    'se': 'nw',
    'sw': 'ne',
    'ne': 'sw',
}

reduce_map = {
    'n': (('sw', 'nw'), ('se', 'ne')),
    'ne': (('nw', 'n'), ('s', 'se')),
    'se': (('n', 'ne'), ('sw', 's')),
    's': (('ne', 'se'), ('nw', 'sw')),
    'sw': (('se', 's'), ('n', 'nw')),
    'nw': (('ne', 'n'), ('s', 'sw')),
}

steps = {
    'nw': 0,
    'n': 0,
    'ne': 0,
    'se': 0,
    's': 0,
    'sw': 0,
}

current = 0
best = 0

for step in input().split(','):
    backtrack_step = backtrack_map[step]
    if steps[backtrack_step] > 0:
        steps[backtrack_step] -= 1
        current -= 1
    else:
        reductions = reduce_map[step]
        found = False
        for pair in reductions:
            if steps[pair[0]] > 0:
                steps[pair[0]] -= 1
                steps[pair[1]] += 1
                found = True
                break
        if not found:
            steps[step] += 1
            current += 1
            best = max(best, current)

print(best)
