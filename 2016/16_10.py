from aocd import get_data, submit
DAY = 10
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split("\n")

bots = {}
outputs = {}
queue = []
pair = (17, 61)

def update(bot, val):
    if 'value1' in bots[bot]:
        bots[bot]['value2'] = val
        queue.append(bot)
    else:
        bots[bot]['value1'] = val

def execute(bot):
    ans = None
    low, high = tuple(sorted([bots[bot]['value1'], bots[bot]['value2']]))
    if (low, high) == pair:
        ans = bot
    if 'low' in bots[bot]:
        if bots[bot]['low']['type'] == 'bot':
            update(bots[bot]['low']['id'], low)
        else:
            outputs[bots[bot]['low']['id']] = low
    if 'high' in bots[bot]:
        if bots[bot]['high']['type'] == 'bot':
            update(bots[bot]['high']['id'], high)
        else:
            outputs[bots[bot]['high']['id']] = high
    return ans

for row in data:
    instr = row.split()
    if instr[0] == 'value':
        if (num := int(instr[-1])) not in bots:
            bots[num] = {}
        update(num, int(instr[1]))
    else:
        if (num := int(instr[1])) not in bots:
            bots[num] = {}
        if instr[5] == 'bot':
            bots[num]['low'] = {'type': 'bot', 'id': int(instr[6])}
        else:
            bots[num]['low'] = {'type': 'output', 'id': int(instr[6])}
        if instr[-2] == 'bot':
            bots[num]['high'] = {'type': 'bot', 'id': int(instr[-1])}
        else:
            bots[num]['high'] = {'type': 'output', 'id': int(instr[-1])}

ans1, ans2 = None, None
while queue:
    curr = queue.pop(0)
    ans = execute(curr)
    if ans is not None:
        ans1 = ans
    if 0 in outputs and 1 in outputs and 2 in outputs:
        ans2 = outputs[0] * outputs[1] * outputs[2]

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)