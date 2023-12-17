import re
import sys

analysis = {
    'children': '3',
    'cats': '7',
    'samoyeds': '2',
    'pomeranians': '3',
    'akitas': '0',
    'vizslas': '0',
    'goldfish': '5',
    'trees': '3',
    'cars': '2',
    'perfumes': '1',
}

for line in sys.stdin.readlines():
    data = re.findall(r'[\w]+', line)
    if analysis[data[2]] == data[3] and analysis[data[4]] == data[5] and analysis[data[6]] == data[7]:
        print(data[1])
        break
