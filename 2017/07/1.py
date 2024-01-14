import re
import sys

seen_base = set()
seen_supported = set()

for line in sys.stdin.readlines():
    parts = re.findall(r'[\w]+', line)
    seen_base.add(parts[0])
    if len(parts) > 2:
        for item in parts[2:]:
            seen_supported.add(item)

print(next(iter(seen_base - seen_supported)))
