steps = {
    'nw': 0,
    'n': 0,
    'ne': 0,
    'se': 0,
    's': 0,
    'sw': 0,
}

for step in input().split(','):
    steps[step] += 1

# remove backtracking steps first
for pair in (('n', 's'), ('ne', 'sw'), ('nw', 'se')):
    amount = min(steps[pair[0]], steps[pair[1]])
    steps[pair[0]] -= amount
    steps[pair[1]] -= amount

# reduce two steps to one
for pair in (
    ('nw', 'n', 'ne'),
    ('n', 'ne', 'se'),
    ('ne', 'se', 's'),
    ('se', 's', 'sw'),
    ('s', 'sw', 'nw'),
    ('sw', 'nw', 'n'),
):
    amount = min(steps[pair[0]], steps[pair[2]])
    if amount > 0:
        steps[pair[0]] -= amount
        steps[pair[2]] -= amount
        steps[pair[1]] += amount

print(sum(steps.values()))
