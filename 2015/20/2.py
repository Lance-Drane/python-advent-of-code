target = int(input())
limit = target // 11
houses = [0] * limit

for house in range(1, limit):
    for boundary in range(house, min(limit, house + house * 50), house):
        houses[boundary] += house * 11
    if houses[house] >= target:
        print(house)
        break
else:
    print(limit)
