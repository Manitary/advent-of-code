from aocd import get_data, submit

DAY = 22
YEAR = 2015

data = get_data(day=DAY, year=YEAR)
boss = tuple(map(int, [row.split()[-1] for row in data.split("\n")]))  # (HP, Atk)
player = (50, 0, 500)  # (HP, Def, Atk)
max_hp = player[0]

# (Magic Missile, Drain, Shield, Poison, Recharge)
spell_cost = (53, 73, 113, 173, 229)
spell_timer = (0, 0, 6, 6, 5)
effect_timer = (0, 0, 0, 0, 0)

# Start of turn effects
def applyEffects(player, boss, effects):
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


def playTurn(player, boss, effects, move, mana, difficulty=0):
    player = list(player)
    boss = list(boss)
    effects = list(effects)
    # Player's move
    player[-1] -= spell_cost[move]
    mana += spell_cost[move]
    effects[move] = spell_timer[move]
    match move:
        case 0:
            boss[0] -= 4
        case 1:
            boss[0] -= 2
            player[0] = min(max_hp, player[0] + 2)
        case 2:
            player[1] = 7
    # Start of boss turn
    player, boss, effects = applyEffects(player, boss, effects)
    # The boss moves only if alive
    if boss[0] > 0:
        # Boss' move
        player[0] -= max(1, boss[1] - player[1])
        # Start of player turn
        player, boss, effects = applyEffects(player, boss, effects)
        if difficulty > 0:
            player[0] -= 1
    return tuple(player), tuple(boss), tuple(effects), mana


def moveChooser(player, effects):
    for i in range(len(effects)):
        if player[-1] >= spell_cost[i] and effects[i] == 0:
            yield i


def findLeastManaBFS(player, boss, difficulty=0):
    visited = set()
    queue = [(player, boss, effect_timer, 0)]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            player, boss, effects, mana = current
            visited.add(current)
            if boss[0] <= 0:
                return mana
            for move in moveChooser(player, effects):
                new_state = playTurn(player, boss, effects, move, mana, difficulty)
                # Only add to the queue if the player is alive
                if new_state[0][0] > 0:
                    queue.append(new_state)
            # Sort by mana spent so far
            queue.sort(key=lambda x: x[-1])


ans1 = findLeastManaBFS(player, boss)
ans2 = findLeastManaBFS(player, boss, 1)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
