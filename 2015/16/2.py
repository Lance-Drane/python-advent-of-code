import re
import sys

analysis = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def is_match(key: str, value: int) -> bool:
    if key in ('cats', 'trees'):
        return value > analysis[key]
    if key in ('pomeranians', 'goldfish'):
        return value < analysis[key]
    return value == analysis[key]


for line in sys.stdin.readlines():
    data = re.findall(r'[\w]+', line)
    if is_match(data[2], int(data[3])) and is_match(data[4], int(data[5])) and is_match(data[6], int(data[7])):
        print(data[1])
        break
