import sys

MARKER = 2503
maxdist = 0

for line in sys.stdin.readlines():
    chunk = line.split(' ')
    speed, travel, rest = int(chunk[3]), int(chunk[6]), int(chunk[-2])
    km = speed * travel
    elapsed = travel + rest

    time = 0
    dist = 0
    while time <= MARKER - elapsed:
        dist += km
        time += elapsed

    remainder = min(MARKER - time, travel)
    if remainder > 0:
        dist += speed * remainder

    maxdist = max(maxdist, dist)

print(maxdist)
