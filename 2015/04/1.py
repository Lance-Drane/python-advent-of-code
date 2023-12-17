import hashlib
from itertools import count

key = input()
for number in count(start=1):
    if hashlib.md5(f'{key}{number}'.encode()).hexdigest()[:5] == '00000':
        break

print(number)
