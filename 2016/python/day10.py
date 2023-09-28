from typing import Any

from aocd import get_data, submit

DAY = 10
YEAR = 2016


def update(bots: dict[int, Any], bot: int, val: int) -> int | None:
    if "value1" in bots[bot]:
        bots[bot]["value2"] = val
        return bot
    bots[bot]["value1"] = val
    return None


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR).split("\n")

    bots: dict[int, Any] = {}
    outputs: dict[int, int] = {}
    queue: list[int] = []
    pair = (17, 61)

    def execute(bots: dict[int, Any], bot: int, outputs: dict[int, int]) -> int:
        ans = -1
        low, high = tuple(sorted([bots[bot]["value1"], bots[bot]["value2"]]))
        if (low, high) == pair:
            ans = bot
        if "low" in bots[bot]:
            if bots[bot]["low"]["type"] == "bot":
                q = update(bots, bots[bot]["low"]["id"], low)
                if q is not None:
                    queue.append(q)
            else:
                outputs[bots[bot]["low"]["id"]] = low
        if "high" in bots[bot]:
            if bots[bot]["high"]["type"] == "bot":
                q = update(bots, bots[bot]["high"]["id"], high)
                if q is not None:
                    queue.append(q)
            else:
                outputs[bots[bot]["high"]["id"]] = high
        return ans

    for row in data:
        instr = row.split()
        if instr[0] == "value":
            if (num := int(instr[-1])) not in bots:
                bots[num] = {}
            q = update(bots, num, int(instr[1]))
            if q is not None:
                queue.append(q)
        else:
            if (num := int(instr[1])) not in bots:
                bots[num] = {}
            if instr[5] == "bot":
                bots[num]["low"] = {"type": "bot", "id": int(instr[6])}
            else:
                bots[num]["low"] = {"type": "output", "id": int(instr[6])}
            if instr[-2] == "bot":
                bots[num]["high"] = {"type": "bot", "id": int(instr[-1])}
            else:
                bots[num]["high"] = {"type": "output", "id": int(instr[-1])}

    part1, part2 = 0, 0
    while queue:
        curr = queue.pop(0)
        ans = execute(bots, curr, outputs)
        if ans >= 0:
            part1 = ans
        if 0 in outputs and 1 in outputs and 2 in outputs:
            part2 = outputs[0] * outputs[1] * outputs[2]
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
