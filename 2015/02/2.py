import sys
from math import prod

feet = 0

for line in sys.stdin.readlines():
    nums = sorted(int(a) for a in line.split('x'))
    feet += nums[0] * 2 + nums[1] * 2 + prod(nums)

print(feet)
