from hashlib import md5
from itertools import count

key = input()
password = []
for number in count(start=0):
    hsh = md5(f'{key}{number}'.encode()).hexdigest()
    if hsh[:5] == '00000':
        password.append(hsh[5])
        if len(password) == 8:
            break

print(''.join(password))
