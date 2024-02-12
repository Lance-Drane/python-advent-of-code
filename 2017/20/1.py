import re
import sys


# order by acceleration first, then velocity, then position
# put index at the end for simplicity
def get_avp(numbers: list[int], idx: int) -> tuple[int, int, int, int]:
    return (
        abs(numbers[6]) + abs(numbers[7]) + abs(numbers[8]),
        abs(numbers[3]) + abs(numbers[4]) + abs(numbers[5]),
        abs(numbers[0]) + abs(numbers[1]) + abs(numbers[2]),
        idx,
    )


print(
    min(get_avp(list(map(int, re.findall(r'-?\d+', line))), idx) for idx, line in enumerate(sys.stdin.readlines()))[3]
)
