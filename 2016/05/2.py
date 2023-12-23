from hashlib import md5
from itertools import count

key = input()
password = [0] * 8
for number in count(start=0):
    hsh = md5(f'{key}{number}'.encode()).hexdigest()
    if hsh[:5] == '00000':
        pos = int(hsh[5], 16)
        if pos < 8 and password[pos] == 0:
            password[pos] = hsh[6]
            if 0 not in password:
                break

print(''.join(password))
