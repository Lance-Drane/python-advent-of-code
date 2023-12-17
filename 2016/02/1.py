import sys

v_pos = 1
h_pos = 2
code = []

for line in sys.stdin.readlines():
    for char in line.rstrip():
        if char == 'U' and v_pos != 0:
            v_pos -= 1
        elif char == 'R' and h_pos != 3:
            h_pos += 1
        elif char == 'D' and v_pos != 2:
            v_pos += 1
        elif char == 'L' and h_pos != 1:
            h_pos -= 1
    code.append(str(v_pos * 3 + h_pos))

print(''.join(code))
