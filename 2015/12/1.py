# note: this code assumes you strip out any commented lines (which may have numbers) from the input
import re
import sys

print(sum(int(a.group()) for a in re.finditer(r'-?\d+', sys.stdin.read())))
