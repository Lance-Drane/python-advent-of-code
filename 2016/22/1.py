import re
import sys

used_list = []
avail_list = []

for line in sys.stdin.readlines()[2:]:
    x, y, size, used, avail, use_percent = map(int, re.findall(r'\d+', line))
    used_list.append((used, x, y))
    avail_list.append((avail, x, y))

used_list = sorted(used_list, key=lambda a: a[0], reverse=True)
while used_list[-1][0] == 0:
    used_list.pop()
used_list.reverse()

avail_list = sorted(avail_list, key=lambda a: a[0], reverse=True)

count = 0
for avail in avail_list:
    if avail[0] < used_list[0][0]:
        break
    for used in used_list:
        if avail[0] >= used[0]:
            if avail[1] != used[1] or avail[2] != used[2]:
                count += 1
        else:
            break

print(count)
