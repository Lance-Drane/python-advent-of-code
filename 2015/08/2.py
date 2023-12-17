import re
import sys

print(sum(len(re.findall(r'[\\"]', line)) + 2 for line in sys.stdin.readlines()))
