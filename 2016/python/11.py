from aocd import get_data, submit
from re import findall
from itertools import combinations, chain
from copy import deepcopy
DAY = 11
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split("\n")

GENERATOR = 'generator'
MICROCHIP = 'microchip'
ELEMENTS = []
TOP = len(data) - 1

floors = []
elevator = 0

regex = r"a (\w+)(?:-compatible)? (microchip|generator)"
for n, row in enumerate(data):
    floors.append(set())
    for f in findall(regex, row):
        if f[0] not in ELEMENTS:
            ELEMENTS.append(f[0])
        floors[-1].add((1 + ELEMENTS.index(f[0])) * (1 if f[1] == GENERATOR else -1))
num_elements = len(ELEMENTS)

def isValid(floor):
    existGenerator = any(x > 0 for x in floor)
    unpairedChip = any(x < 0 and -x not in floor for x in floor)
    return not(existGenerator and unpairedChip)

def getState(floors, elevator):
    '''
    Record the relative position of each microchip/generator pair
    Used to compare floor states that are identical up to permutation of the elements
    '''
    positions = [[None]*2 for _ in range(num_elements)]
    for f, floor in enumerate(floors):
        for i in floor:
            positions[abs(i) - 1][0 if i > 0 else 1] = f
    return (elevator,) + tuple(tuple(x) for x in sorted(positions))

def isWin(floors):
    for f, floor in enumerate(floors):
        if f < TOP and floor:
            return False
    return True

def moves(floors, elevator):
    pairs = tuple(combinations(floors[elevator], 2))
    singles = tuple(({x} for x in floors[elevator]))
    for direction in (1, -1):
        new_elevator = elevator + direction
        if 0 <= new_elevator <= TOP:
            payloads = chain(pairs, singles) if direction > 0 else chain(singles, pairs)
            for payload in payloads:
                new_floors = deepcopy(floors)
                new_floors[elevator] -= set(payload)
                if not isValid(new_floors[elevator]):
                    continue
                new_floors[new_elevator] |= set(payload)
                if not isValid(new_floors[new_elevator]):
                    continue
                yield new_floors, new_elevator

def BFS():
    visited = set()
    queue = [(floors, elevator, getState(floors, elevator), 0)]
    while queue:
        current_floors, current_elevator, current_state, steps = queue.pop(0)
        if isWin(current_floors):
            return steps
        if current_state not in visited:
            visited.add(current_state)
            for new_floors, new_elevator in moves(current_floors, current_elevator):
                new_state = getState(new_floors, new_elevator)
                if new_state not in visited:
                    queue.append((new_floors, new_elevator, new_state, steps + 1))

ans1 = BFS()

NEW_ELEMENTS = 2
for i in range(NEW_ELEMENTS):
    num_elements += 1
    for j in (-1, 1):
        floors[0].add(j*(num_elements))

ans2 = BFS()

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)