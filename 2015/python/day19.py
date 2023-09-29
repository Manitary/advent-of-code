import re
from collections import OrderedDict, defaultdict, deque
from typing import Iterator

from aocd import get_data, submit

DAY = 19
YEAR = 2015

RE_RULE = re.compile(r"(\w+) => (\w+)")
RE_MOLECULE = re.compile(r"(\w+)$")


def find_next(rules: dict[str, list[str]], molecule: str) -> int:
    return len(
        {
            f"{molecule[:m.start()]}{craft}{molecule[m.start() + len(source):]}"
            for source, products in rules.items()
            for craft in products
            for m in re.finditer(source, molecule)
        }
    )


def find_all_previous(rules_rev: dict[str, str], molecule: str) -> Iterator[str]:
    for craft, source in rules_rev.items():
        for m in re.finditer(craft, molecule):
            yield f"{molecule[:m.start()]}{source}{molecule[m.start() + len(craft):]}"


# This will not work and probably run out of memory
def find_shortest_craft_bfs(
    rules_rev: dict[str, str], molecule: str, target: str
) -> int:
    visited: set[str] = set()
    queue: deque[tuple[str, int]] = deque([(molecule, 0)])
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        if current in visited:
            continue
        visited.add(current)
        for previous in find_all_previous(rules_rev, current):
            if previous not in visited:
                queue.append((previous, steps + 1))
    raise ValueError("No path found")


def find_all_previous_greedy(rules_rev: dict[str, str], molecule: str) -> Iterator[str]:
    for craft, source in rules_rev.items():
        for m in reversed(list(re.finditer(craft, molecule))):
            yield f"{molecule[:m.start()]}{source}{molecule[m.start() + len(craft):]}"


# Greedy algorithm; it works because the solution is actually unique
def find_shortest_craft_greedy_dfs(
    rules_rev: dict[str, str], molecule: str, target: str, steps: int = 0
) -> int:
    if molecule == target:
        return steps
    for previous in find_all_previous_greedy(rules_rev, molecule):
        return find_shortest_craft_greedy_dfs(rules_rev, previous, target, steps + 1)
    raise ValueError("Solution not found")


# Explanation at https://old.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4h7ji/
def find_shortest_craft(molecule: str) -> int:
    return (
        len([x for x in molecule if x.isupper()])
        - molecule.count("Rn")
        - molecule.count("Ar")
        - 2 * molecule.count("Y")
        - 1
    )


def main() -> tuple[int, int, int]:
    data = get_data(day=DAY, year=YEAR)
    molecule: str = RE_MOLECULE.findall(data)[0]
    rules: dict[str, list[str]] = defaultdict(list)
    rules_rev: dict[str, str] = {}
    for rule in RE_RULE.findall(data):
        rules[rule[0]].append(rule[1])
        rules_rev[rule[1]] = rule[0]
    rules_rev_sorted = OrderedDict(
        reversed(sorted(rules_rev.items(), key=lambda x: len(x[0])))
    )

    part1 = find_next(rules, molecule)
    part2 = find_shortest_craft(molecule)
    part2a = find_shortest_craft_greedy_dfs(rules_rev_sorted, molecule, "e")
    return part1, part2, part2a


if __name__ == "__main__":
    ans1, ans2, ans2a = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
    submit(ans2a, part="b", day=DAY, year=YEAR)
