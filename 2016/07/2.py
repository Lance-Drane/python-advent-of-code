import re
import sys
from itertools import chain


def get_abas(string):
    for i in range(len(string) - 2):
        if string[i] != string[i + 1] and string[i] == string[i + 2]:
            yield string[i : i + 3]


def aba_2_bab(string):
    a = string[0]
    b = string[1]
    return f'{b}{a}{b}'


count = 0

for line in sys.stdin.readlines():
    parts = re.split(r'[\[\]]', line.rstrip())
    if set(chain(*(get_abas(s) for s in parts[::2]))) & set(map(aba_2_bab, chain(*(get_abas(s) for s in parts[1::2])))):
        count += 1
print(count)
