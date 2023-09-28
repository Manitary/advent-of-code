from aocd import get_data, submit
from intcode import Computer

DAY = 23
YEAR = 2019


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    network = [Computer(data) for _ in range(50)]
    for i, pc in enumerate(network):
        pc.push(i)

    part1 = 0
    nat: list[int] = []
    last_nat: list[int] = []

    while True:
        idle = True
        for pc in network:
            if not pc.input:
                pc.push(-1)
            else:
                idle = False
            pc.run()
            while len(pc.output) >= 3:
                address, x, y = pc.pop_many(3)
                if address < len(network):
                    network[address].push([x, y])
                if address != 255:
                    continue
                if not part1:
                    part1 = y
                nat = [x, y]
        if not (idle and nat):
            continue
        network[0].push(nat)
        if nat == last_nat:
            part2 = nat[1]
            break
        last_nat = nat

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
