target = int(input())
houses = [10] * (target // 10)

for house in range(2, target // 10):
    for boundary in range(house, target // 10, house):
        houses[boundary] += house * 10
    if houses[house] >= target:
        print(house)
        break
else:
    print(target // 10)
