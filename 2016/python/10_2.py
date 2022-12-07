from aocd import get_data, submit
from collections import defaultdict

DAY = 10
YEAR = 2016

data = get_data(day=DAY, year=YEAR).split("\n")

queue = []


class Bot:
    def __init__(self):
        self.values = []
        self.high = None
        self.low = None

    def addValue(self, value):
        self.values.append(value)
        if len(self.values) == 2:
            queue.append(self)

    def sortValues(self):
        self.values = sorted(self.values)

    def giveValues(self):
        self.sortValues()
        self.low.addValue(self.values[0])
        self.high.addValue(self.values[1])


class Output:
    def __init__(self):
        self.value = None

    def addValue(self, value):
        self.value = value


bots = defaultdict(Bot)
outputs = defaultdict(Output)

for row in data:
    instr = row.split()
    if instr[0] == "value":
        num = int(instr[-1])
        bots[num].addValue(int(instr[1]))
    else:
        num, low, high = int(instr[1]), int(instr[6]), int(instr[-1])
        if instr[5] == "bot":
            bots[num].low = bots[low]
        else:
            bots[num].low = outputs[low]
        if instr[-2] == "bot":
            bots[num].high = bots[high]
        else:
            bots[num].high = outputs[high]

pair = {17, 61}
ans1, ans2 = None, None
while queue:
    curr = queue.pop(0)
    if (not ans1) and set(curr.values) == pair:
        ans1 = tuple(bots)[tuple(bots.values()).index(curr)]
    curr.giveValues()
    if (not ans2) and outputs[0].value and outputs[1].value and outputs[2].value:
        ans2 = outputs[0].value * outputs[1].value * outputs[2].value
    if ans1 and ans2:
        break

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
