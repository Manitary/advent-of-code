from itertools import combinations
from re import findall

from aocd import get_data, submit
from intcode import Computer

DAY = 25
YEAR = 2019


PATH = [
    "west",
    "west",
    "west",
    "take coin",
    "east",
    "east",
    "east",
    "north",
    "north",
    "take mutex",
    "east",
    "take antenna",
    "west",
    "south",
    "east",
    "take cake",
    "east",
    "north",
    "take pointer",
    "south",
    "west",
    "west",
    "south",
    "east",
    "east",
    "take tambourine",
    "east",
    "take fuel cell",
    "east",
    "take boulder",
    "north",
]

ITEMS = {
    "coin",
    "mutex",
    "antenna",
    "cake",
    "pointer",
    "tambourine",
    "fuel cell",
    "boulder",
}


def speak(droid: Computer) -> str:
    return "".join(list(map(chr, droid.pop_many(len(droid.output)))))


def convertInput(droid: Computer, string: str = "") -> str:
    droid.push(list(map(ord, list(string))) + [10])
    droid.run()
    return speak(droid)


def dropAll(droid: Computer) -> None:
    for item in ITEMS:
        convertInput(droid, f"drop {item}")


def play() -> None:
    """Play the game manually"""
    data = get_data(day=DAY, year=YEAR)
    droid = Computer(data)
    droid.run()
    print(speak(droid))
    while True:
        instruction = input("Enter instruction: ")
        if instruction in {"q", "Q", "quit"}:
            break
        if instruction in {"r", "R", "restart"}:
            droid.reset()
            droid.run()
            print(speak(droid))
        output = convertInput(droid, instruction)
        print(output)


def main() -> int:
    data = get_data(day=DAY, year=YEAR)
    droid = Computer(data)
    droid.run()
    for instruction in PATH:
        convertInput(droid, instruction)

    last_output = ""
    ans1 = 0
    for i in range(len(ITEMS)):
        for items in combinations(ITEMS, i):
            dropAll(droid)
            for item in items:
                convertInput(droid, f"take {item}")
            output = convertInput(droid, "east")
            if output:
                last_output = output
            else:
                ans1 = int(findall(r"\d+", last_output)[0])
                break
        else:
            continue
        break
    return ans1


if __name__ == "__main__":
    ans1 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
