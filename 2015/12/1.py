# note: this code assumes you strip out any commented lines (which may have numbers) from the input
import re
import sys

print(sum(int(a) for a in re.findall(r'-?\d+', sys.stdin.read())))
