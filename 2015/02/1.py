import sys

feet = 0

for line in sys.stdin.readlines():
    nums = tuple(int(a) for a in line.split('x'))
    sides = (nums[0] * nums[1], nums[1] * nums[2], nums[2] * nums[0])
    feet += sum(2 * a for a in sides) + min(sides)

print(feet)
