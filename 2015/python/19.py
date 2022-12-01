from aocd import get_data, submit
from re import findall, finditer
from collections import defaultdict, deque, OrderedDict
DAY = 19
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

rules = defaultdict(list)
rules_rev = {}

rule_pattern = r"(\w+) => (\w+)"
for rule in findall(rule_pattern, data):
    rules[rule[0]].append(rule[1])
    rules_rev[rule[1]] = rule[0]

molecule_pattern = r"(\w+)$"
molecule = findall(molecule_pattern, data)[0]

start = "e"

def findNext(molecule: str):
    candidates = set()
    for source, products in rules.items():
        for craft in products:
            for m in finditer(source, molecule):
                candidates.add(f"{molecule[:m.start()]}{craft}{molecule[m.start() + len(source):]}")
    return len(candidates)

def findAllPrevious(molecule: str):
    for craft, source in rules_rev.items():
        for m in finditer(craft, molecule):
            yield f"{molecule[:m.start()]}{source}{molecule[m.start() + len(craft):]}"

#This will not work and probably run out of memory
def findShortestCraftBFS(molecule: str, target: str):
    visited = set()
    queue = deque([(molecule, 0)])
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        if current not in visited:
            visited.add(current)
            for previous in findAllPrevious(current):
                if previous not in visited:
                    queue.append((previous, steps + 1))

rules_rev_sorted = OrderedDict(reversed(sorted(rules_rev.items(), key = lambda x: len(x[0]))))

def findAllPreviousGreedy(molecule: str):
    for craft, source in rules_rev_sorted.items():
        for m in reversed([x for x in finditer(craft, molecule)]):
            yield f"{molecule[:m.start()]}{source}{molecule[m.start() + len(craft):]}"
    raise StopIteration

#Greedy algorithm; it works because the solution is actually unique
def findShortestCraftGreedyDFS(molecule: str, target:str, steps: int = 0):
    if molecule == target:
        return steps
    for previous in findAllPreviousGreedy(molecule):
        return findShortestCraftGreedyDFS(previous, target, steps + 1)

#The clever solution; explanation at https://old.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4h7ji/
def findShortestCraft(molecule: str):
    return len([x for x in molecule if x.isupper()]) - molecule.count("Rn") - molecule.count("Ar") - 2 * molecule.count("Y") - 1

ans1 = findNext(molecule)
ans2 = findShortestCraft(molecule)
ans2a = findShortestCraftGreedyDFS(molecule, start)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
submit(ans2a, part="b", day=DAY, year=YEAR)