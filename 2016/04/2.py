import sys
from collections import Counter

for line in sys.stdin.readlines():
    parts = line.split('-')
    encrypted_room = ''.join(parts[:-1])
    if line.rstrip()[-6:-1] == ''.join(p[0] for p in Counter(sorted(encrypted_room)).most_common(5)):
        sector_id = int(parts[-1][: parts[-1].find('[')])
        num_shifts = sector_id % 26
        decrypt = ''.join([chr(a - 26) if a > 122 else chr(a) for a in (ord(c) + num_shifts for c in encrypted_room)])
        if decrypt.startswith('northpole'):
            print(sector_id)
            break
