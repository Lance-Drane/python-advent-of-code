import operator
import sys
from collections import defaultdict

registers: defaultdict[str, int] = defaultdict(int)
operations = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
}

for line in sys.stdin.readlines():
    parts = line.split()
    register_check_val = registers[parts[4]]
    check_val = int(parts[6])
    if operations[parts[5]](register_check_val, check_val):
        if parts[1] == 'inc':
            registers[parts[0]] += int(parts[2])
        else:
            registers[parts[0]] -= int(parts[2])

print(max(registers.values()))
