import sys
from typing import TypedDict


class Effects(TypedDict):
    shield: int
    poison: int
    recharge: int


MAGIC_MISSLE = 53
DRAIN = 73
SHIELD = 113
POISON = 173
RECHARGE = 229

for line in sys.stdin.readlines():
    attr, value = line.split(': ')
    if attr == 'Damage':
        boss_damage = int(value)
    else:
        boss_start_hp = int(value)


def take_turn(  # noqa: PLR0913
    player_turn: bool,  # noqa: FBT001
    player_hp: int,
    player_mana: int,
    spent_mana: int,
    boss_hp: int,
    effects: Effects,
) -> int:
    """
    if infinity gets returned, either the player couldn't cast a spell
    or died to the boss attack
    """
    # hard mode
    if player_turn:
        next_player_hp = player_hp - 1
        if next_player_hp == 0:
            # player dies
            return float('inf')
    else:
        next_player_hp = player_hp

    # apply effects
    next_boss_hp = boss_hp
    if effects['poison'] > 0:
        next_boss_hp -= 3
        if next_boss_hp <= 0:
            # boss dies
            return spent_mana
    next_player_mana = player_mana
    if effects['recharge'] > 0:
        next_player_mana += 101

    # countdown effects
    next_effects = effects.copy()
    for effect, turns in next_effects.items():
        next_effects[effect] = max(turns - 1, 0)

    # handle boss turn
    if not player_turn:
        player_armor = 7 if effects['shield'] > 0 else 0
        new_player_hp = next_player_hp - max(boss_damage - player_armor, 1)
        if new_player_hp <= 0:
            # player dies
            return float('inf')
        return take_turn(
            player_turn=True,
            player_hp=new_player_hp,
            player_mana=next_player_mana,
            spent_mana=spent_mana,
            boss_hp=next_boss_hp,
            effects=next_effects,
        )

    # handle player turn - check cheapest spells first
    # do not cast effect spells if already active
    # only need to check magic missile to see if the boss dies
    best = float('inf')  # player "dies" if no spell can be cast
    # magic missile
    if next_player_mana >= MAGIC_MISSLE:
        if next_boss_hp <= 4:
            # boss dies
            return spent_mana + MAGIC_MISSLE
        best = min(
            best,
            take_turn(
                player_turn=False,
                player_hp=next_player_hp,
                player_mana=next_player_mana - MAGIC_MISSLE,
                spent_mana=spent_mana + MAGIC_MISSLE,
                boss_hp=next_boss_hp - 4,
                effects=next_effects,
            ),
        )
    # drain
    if next_player_mana >= DRAIN:
        best = min(
            best,
            take_turn(
                player_turn=False,
                player_hp=next_player_hp + 2,
                player_mana=next_player_mana - DRAIN,
                spent_mana=spent_mana + DRAIN,
                boss_hp=next_boss_hp - 2,
                effects=next_effects,
            ),
        )
    # shield
    if next_player_mana >= SHIELD and next_effects['shield'] == 0:
        local_effects = next_effects.copy()
        local_effects['shield'] = 6
        best = min(
            best,
            take_turn(
                player_turn=False,
                player_hp=next_player_hp,
                player_mana=next_player_mana - SHIELD,
                spent_mana=spent_mana + SHIELD,
                boss_hp=next_boss_hp,
                effects=local_effects,
            ),
        )
    # poison
    if next_player_mana >= POISON and next_effects['poison'] == 0:
        local_effects = next_effects.copy()
        local_effects['poison'] = 6
        best = min(
            best,
            take_turn(
                player_turn=False,
                player_hp=next_player_hp,
                player_mana=next_player_mana - POISON,
                spent_mana=spent_mana + POISON,
                boss_hp=next_boss_hp,
                effects=local_effects,
            ),
        )
    # recharge
    if next_player_mana >= RECHARGE and next_effects['recharge'] == 0:
        local_effects = next_effects.copy()
        local_effects['recharge'] = 5
        best = min(
            best,
            take_turn(
                player_turn=False,
                player_hp=next_player_hp,
                player_mana=next_player_mana - RECHARGE,
                spent_mana=spent_mana + RECHARGE,
                boss_hp=next_boss_hp,
                effects=local_effects,
            ),
        )
    return best


print(
    take_turn(
        player_turn=True,
        player_hp=50,
        player_mana=500,
        spent_mana=0,
        boss_hp=boss_start_hp,
        effects=Effects(shield=0, poison=0, recharge=0),
    )
)
