import re
from copy import deepcopy
from itertools import chain, combinations
from typing import Generator

from aocd import get_data, submit

DAY = 11
YEAR = 2016

Floor = set[int]
State = tuple[int | tuple[int, ...], ...]

GENERATOR = "generator"
MICROCHIP = "microchip"
PATTERN = re.compile(r"a (\w+)(?:-compatible)? (microchip|generator)")


def is_valid(floor: Floor) -> bool:
    exist_generator = any(x > 0 for x in floor)
    unpaired_chip = any(x < 0 and -x not in floor for x in floor)
    return not (exist_generator and unpaired_chip)


def is_win(floors: list[Floor]) -> bool:
    return not any(floors[:-1])


def get_state(floors: list[Floor], elevator: int, num_elements: int) -> State:
    """
    Record the relative position of each microchip/generator pair
    Used to compare floor states that are identical up to permutation of the elements
    """
    positions: list[list[int]] = [[0, 0] for _ in range(num_elements)]
    for f, floor in enumerate(floors):
        for i in floor:
            positions[abs(i) - 1][0 if i > 0 else 1] = f
    return (elevator,) + tuple(tuple(x) for x in sorted(positions))


def moves(
    floors: list[Floor], elevator: int
) -> Generator[tuple[list[Floor], int], None, None]:
    pairs = tuple(combinations(floors[elevator], 2))
    singles = tuple(({x} for x in floors[elevator]))
    for direction in (1, -1):
        new_elevator = elevator + direction
        if not 0 <= new_elevator <= len(floors) - 1:
            continue
        payloads = chain(pairs, singles) if direction > 0 else chain(singles, pairs)
        for payload in payloads:
            new_floors = deepcopy(floors)
            new_floors[elevator] -= set(payload)
            if not is_valid(new_floors[elevator]):
                continue
            new_floors[new_elevator] |= set(payload)
            if not is_valid(new_floors[new_elevator]):
                continue
            yield new_floors, new_elevator


def bfs(floors: list[Floor], elevator: int, num_elements: int) -> int:
    visited: set[State] = set()
    queue: list[tuple[list[Floor], int, State, int]] = [
        (floors, elevator, get_state(floors, elevator, num_elements), 0)
    ]
    while queue:
        current_floors, current_elevator, current_state, steps = queue.pop(0)
        if is_win(current_floors):
            return steps
        if current_state in visited:
            continue
        visited.add(current_state)
        for new_floors, new_elevator in moves(current_floors, current_elevator):
            new_state = get_state(new_floors, new_elevator, num_elements)
            if new_state not in visited:
                queue.append((new_floors, new_elevator, new_state, steps + 1))
    raise ValueError("No path found")


def parse_input(data: list[str]) -> tuple[list[Floor], list[str]]:
    floors: list[set[int]] = []
    elements: list[str] = []
    for row in data:
        floors.append(set())
        for f in PATTERN.findall(row):
            if f[0] not in elements:
                elements.append(f[0])
            floors[-1].add(
                (1 + elements.index(f[0])) * (1 if f[1] == GENERATOR else -1)
            )
    return floors, elements


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")

    floors, elements = parse_input(data)
    part1 = bfs(floors, 0, len(elements))

    floors, elements = parse_input(data)
    new_elements = 2
    for i in range(1, new_elements + 1):
        for j in (-1, 1):
            floors[0].add(j * (len(elements) + i))

    part2 = bfs(floors, 0, len(elements) + new_elements)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
