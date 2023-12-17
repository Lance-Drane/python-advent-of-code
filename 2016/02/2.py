import sys

keypad = (
    (
        '',
        '',
        '1',
        '',
        '',
    ),
    (
        '',
        '2',
        '3',
        '4',
        '',
    ),
    (
        '5',
        '6',
        '7',
        '8',
        '9',
    ),
    (
        '',
        'A',
        'B',
        'C',
        '',
    ),
    (
        '',
        '',
        'D',
        '',
        '',
    ),
)
v_pos = 2
h_pos = 0
code = []

for line in sys.stdin.readlines():
    for char in line.rstrip():
        if char == 'U' and v_pos != 0 and keypad[v_pos - 1][h_pos] != '':
            v_pos -= 1
        elif char == 'R' and h_pos != 4 and keypad[v_pos][h_pos + 1] != '':
            h_pos += 1
        elif char == 'D' and v_pos != 4 and keypad[v_pos + 1][h_pos] != '':
            v_pos += 1
        elif char == 'L' and h_pos != 0 and keypad[v_pos][h_pos - 1] != '':
            h_pos -= 1
    code.append(keypad[v_pos][h_pos])

print(''.join(code))
