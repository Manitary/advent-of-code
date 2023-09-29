from typing import Iterator, Sequence

from aocd import get_data, submit

DAY = 22
YEAR = 2015

# (Magic Missile, Drain, Shield, Poison, Recharge)
SPELL_COST = (53, 73, 113, 173, 229)
SPELL_TIMER = (0, 0, 6, 6, 5)
PLAYER = (50, 0, 500)  # (HP, Def, Atk)
MAX_HP = PLAYER[0]


# Start of turn effects
def apply_effects(
    player: list[int], boss: list[int], effects: list[int]
) -> tuple[list[int], list[int], list[int]]:
    for i, t in enumerate(effects):
        if t > 0:
            if i == 3:
                boss[0] -= 3
            elif i == 4:
                player[-1] += 101
            effects[i] -= 1
        elif i == 2:
            player[1] = 0
    return player, boss, effects


def play_turn(
    player: Sequence[int],
    boss: Sequence[int],
    effects: Sequence[int],
    move: int,
    mana: int,
    difficulty: int = 0,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], int]:
    player = list(player)
    boss = list(boss)
    effects = list(effects)
    # Player's move
    player[-1] -= SPELL_COST[move]
    mana += SPELL_COST[move]
    effects[move] = SPELL_TIMER[move]
    if move == 0:
        boss[0] -= 4
    elif move == 1:
        boss[0] -= 2
        player[0] = min(MAX_HP, player[0] + 2)
    elif move == 2:
        player[1] = 7
    # Start of boss turn
    player, boss, effects = apply_effects(player, boss, effects)
    # The boss moves only if alive
    if boss[0] > 0:
        # Boss' move
        player[0] -= max(1, boss[1] - player[1])
        # Start of player turn
        player, boss, effects = apply_effects(player, boss, effects)
        if difficulty > 0:
            player[0] -= 1
    return tuple(player), tuple(boss), tuple(effects), mana


def move_chooser(player: tuple[int, ...], effects: tuple[int, ...]) -> Iterator[int]:
    for i, e in enumerate(effects):
        if player[-1] >= SPELL_COST[i] and e == 0:
            yield i


def find_least_mana_bfs(
    player: tuple[int, ...],
    boss: tuple[int, ...],
    effect_timer: tuple[int, ...],
    difficulty: int = 0,
) -> int:
    visited: set[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], int]] = set()
    queue: list[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], int]] = [
        (player, boss, effect_timer, 0)
    ]
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        player, boss, effects, mana = current
        visited.add(current)
        if boss[0] <= 0:
            return mana
        queue.extend(
            new_state
            for move in move_chooser(player, effects)
            if (new_state := play_turn(player, boss, effects, move, mana, difficulty))[
                0
            ][0]
            > 0  # Only add to the queue if the player is alive
        )
        queue.sort(key=lambda x: x[-1])  # Sort by mana spent so far
    raise ValueError("Cannot defeat the boss")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    boss = tuple(map(int, [row.split()[-1] for row in data.split("\n")]))  # (HP, Atk)
    part1 = find_least_mana_bfs(PLAYER, boss, (0,) * len(SPELL_TIMER))
    part2 = find_least_mana_bfs(PLAYER, boss, (0,) * len(SPELL_TIMER), 1)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
