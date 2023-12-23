import re

row, column = map(int, re.findall(r'[\d]+', input()))

nth_code = 0
for i in range(2, column + 1):
    nth_code += i
for i in range(2, row + 1):
    nth_code += column + i - 2

code = 20151125
for _ in range(nth_code):
    code = code * 252533 % 33554393
print(code)
