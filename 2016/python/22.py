from aocd import submit, get_data
from re import search, compile
from itertools import product
DAY = 22
YEAR = 2016

data = get_data(day=DAY, year=YEAR)
data = [row.split() for row in data.split('\n')]

pattern = r"x(\d+)-y(\d+)"
compile(pattern)
nodes = {tuple(map(int, search(pattern, row[0]).groups())): {'size': int(row[1][:-1]), 'used': int(row[2][:-1]), 'avail': int(row[3][:-1])} for row in data[2:]}

def part1():
    ans = 0
    for node1, node2 in product(nodes, nodes):
        if node1 == node2:
            continue
        if 0 < nodes[node1]['used'] <= nodes[node2]['avail']:
            ans += 1
    return ans

maxX = max(node[0] for node in nodes)
maxY = max(node[1] for node in nodes)
target_cell = (0, 0)
data_position = (maxX, 0)

'''
Properties of the input we can exploit:
* There is only one "free node" (with no data).
* No data can be merged, the only possible moves are moving data into the free node.
* There is a bunch of nodes with too much data that is impossible to move around.
Hence, the only information needed is the location of the data we want, and of the free cell;
we don't need to store anything else to keep track of visited states for a BFS.
'''
free_node = [node for node, value in nodes.items() if value['used'] == 0][0]
unavailable = {node for node, value in nodes.items() if value['used'] > 400}

def availableMoves(node):
    x, y = node
    candidates = ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
    for c in candidates:
        if c not in unavailable and 0 <= c[0] <= maxX and 0 <= c[1] <= maxY:
            yield c

def part2BFS(target, start):
    visited = set()
    queue = [(start, free_node, 0)]
    while queue:
        current_goal, current_free, steps = queue.pop(0)
        if current_goal == target:
            return steps
        if (current_goal, current_free) not in visited:
            visited.add((current_goal, current_free))
            for move in availableMoves(current_free):
                new_free = move
                if current_goal == move:
                    new_goal = current_free
                else:
                    new_goal = current_goal
                queue.append((new_goal, new_free, steps + 1))

ans1 = part1()
ans2 = part2BFS(target_cell, data_position)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part = "b", day=DAY, year=YEAR)