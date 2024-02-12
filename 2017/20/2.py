import math
import re
import sys
from collections import defaultdict
from itertools import combinations

particles = [tuple(map(int, re.findall(r'-?\d+', line))) for line in sys.stdin.readlines()]


def solve_quadratic(p1: int, p2: int, v1: int, v2: int, a1: int, a2: int) -> tuple[float, float]:
    a = (a1 - a2) / 2
    b = (v1 - v2) + a
    c = p1 - p2
    discriminant = (b**2) - (4 * a * c)
    if discriminant < 0:
        # no solutions
        return ()
    if discriminant == 0:
        return ((-b / (2 * a)),)
    return (
        (-b + math.sqrt(discriminant)) / (2 * a),
        (-b - math.sqrt(discriminant)) / (2 * a),
    )


def solve_linear(p1: int, p2: int, v1: int, v2: int) -> float:
    return (p2 - p1) / (v1 - v2)


def solve(p1: int, p2: int, v1: int, v2: int, a1: int, a2: int) -> set[int]:
    """Find the positive integer points in time where P1 and P2 intersect

    Returns a set with points in time.

    Credit to the underlying math goes to mjpieters - https://github.com/mjpieters/adventofcode/blob/master/2017/Day%2020.ipynb
    """
    ts = (solve_linear(p1, p2, v1, v2),) if a1 == a2 else solve_quadratic(p1, p2, v1, v2, a1, a2)
    return {int(round(t)) for t in ts if t > 0 and math.isclose(t, round(t))}


def get_collision_time(one: list[int], two: list[int]) -> int | None:
    solutions = None
    for idx in range(3):
        p1, v1, a1 = one[idx], one[idx + 3], one[idx + 6]
        p2, v2, a2 = two[idx], two[idx + 3], two[idx + 6]
        if a1 == a2 and v1 == v2:
            if p1 == p2:
                # parallel paths
                continue
            # will never cross
            return None
        if solutions is None:
            solutions = solve(p1, p2, v1, v2, a1, a2)
        else:
            solutions &= solve(p1, p2, v1, v2, a1, a2)
        if not solutions:
            return None
    return min(solutions)


# original ugly brute-force solution, iterate over each tic in time until you manually notice the length of the particles array not getting any smaller
# when reading in particles, just read each into a list instead of a tuple
# this is techincally "faster" but involves guesswork
"""
for _ in range(39):
    collisions = defaultdict(list)
    for particle in particles:
        particle[3] += particle[6]
        particle[4] += particle[7]
        particle[5] += particle[8]
        particle[0] += particle[3]
        particle[1] += particle[4]
        particle[2] += particle[5]
        collisions[(particle[0], particle[1], particle[2])].append(particle)

    for matches in collisions.values():
        if len(matches) >= 2:
            for match in matches:
                particles.remove(match)

print(len(particles))
"""

# get collisions by time
collisions = defaultdict(set)
for one, two in combinations(particles, 2):
    time = get_collision_time(one, two)
    if time is not None:
        collisions[time] |= {one, two}

# account for particles which are "safe" thanks to earlier collisions
eliminated = set()
for _, collided in sorted(collisions.items()):
    for one, two in combinations(collided - eliminated, 2):
        eliminated |= {one, two}

print(len(particles) - len(eliminated))
