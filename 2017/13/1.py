import sys


class Scanner:
    def __init__(self, scanner_range: int):
        self.scanner_range = scanner_range
        self.position = 1
        self.incrementing = True

    def tick(self):
        if self.incrementing:
            self.position += 1
            if self.position == self.scanner_range:
                self.incrementing = False
        else:
            self.position -= 1
            if self.position == 1:
                self.incrementing = True


graph: dict[int, Scanner] = {}
highest = -1
for line in sys.stdin.readlines():
    key, value = line.split(': ')
    key = int(key)
    graph[key] = Scanner(int(value))
    highest = max(highest, key)

highest += 1
severity = 0
for depth in range(highest):
    current_scanner = graph.get(depth)
    if current_scanner and current_scanner.position == 1:
        severity += depth * current_scanner.scanner_range
    for scanner in graph.values():
        scanner.tick()

print(severity)
