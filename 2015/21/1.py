import sys

# pre-sort everything by cost
weapons = (
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
)
armor = (
    (0, 0, 0),  # no armor
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
)
rings = (
    (0, 0, 0),  # no ring
    (0, 0, 0),  # no ring
    (20, 0, 1),
    (25, 1, 0),
    (40, 0, 2),
    (50, 2, 0),
    (80, 0, 3),
    (100, 3, 0),
)

boss_hp = 0
boss_damage = 0
boss_armor = 0


def win_battle(player_damage, player_armor):
    player_hp = 100
    boss_hp_local = boss_hp
    while player_hp > 0 and boss_hp_local > 0:
        boss_hp_local -= max(player_damage - boss_armor, 1)
        player_hp -= max(boss_damage - player_armor, 1)
    # check boss HP, as player goes first
    return boss_hp_local <= 0


for line in sys.stdin.readlines():
    attr, value = line.split(': ')
    if attr == 'Damage':
        boss_damage = int(value)
    elif attr == 'Armor':
        boss_armor = int(value)
    else:
        boss_hp = int(value)

best = float('inf')
for w_cost, w_damage, w_armor in weapons:
    for a_cost, a_damage, a_armor in armor:
        for idx, (r1_cost, r1_damage, r1_armor) in enumerate(rings):
            for r2_cost, r2_damage, r2_armor in rings[idx + 1 :]:
                if win_battle(
                    w_damage + a_damage + r1_damage + r2_damage, w_armor + a_armor + r1_armor + r2_armor
                ):
                    best = min(best, w_cost + a_cost + r1_cost + r2_cost)

print(best)
