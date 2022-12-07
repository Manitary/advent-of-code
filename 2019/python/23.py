from aocd import get_data, submit
from intcode import Computer

DAY = 23
YEAR = 2019

data = get_data(day=DAY, year=YEAR)
network = [Computer(data) for _ in range(50)]
for i, pc in enumerate(network):
    pc.push(i)

ans1 = None
NAT = None
lastNAT = None

while True:
    idle = True
    for pc in network:
        if not pc.input:
            pc.push(-1)
        else:
            idle = False
        pc.run()
        while len(pc.output) >= 3:
            address, x, y = pc.pop(3)
            if address < len(network):
                network[address].push([x, y])
            if address == 255:
                if not ans1:
                    ans1 = y
                NAT = [x, y]
    if idle and NAT:
        network[0].push(NAT)
        if NAT == lastNAT:
            ans2 = NAT[1]
            break
        lastNAT = NAT

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
