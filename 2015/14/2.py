import sys

MARKER = 2503


class Reindeer:
    def __init__(self, speed, travel, rest):
        self.speed = speed
        self.travel_time = travel
        self.rest_time = rest
        self.points = 0
        self.distance = 0
        self.countdown = travel
        self.moving = True

    def tick(self):
        if self.moving:
            self.distance += self.speed
        self.countdown -= 1
        if self.countdown == 0:
            self.moving = not self.moving
            self.countdown = self.travel_time if self.moving else self.rest_time


reindeer = []

for line in sys.stdin.readlines():
    chunk = line.split(' ')
    reindeer.append(Reindeer(int(chunk[3]), int(chunk[6]), int(chunk[-2])))

for _ in range(MARKER):
    for r in reindeer:
        r.tick()
    maxdist = max(p.distance for p in reindeer)
    for leader in filter(lambda a: a.distance == maxdist, reindeer):
        leader.points += 1

print(max(p.points for p in reindeer))
