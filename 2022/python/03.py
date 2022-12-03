from aocd import get_data, submit
from typing import Iterable
from itertools import starmap

def itemPriority(char: str) -> int:
    return 1 + ord(char) - ord('a') if char.islower() else 27 + ord(char) - ord('A')

def groupPriority(*string_list: Iterable[str]) -> int:
    return itemPriority(set.intersection(*(set(x) for x in string_list)).pop())

def stringPriority(string: str) -> int:
    return groupPriority(string[:len(string)//2], string[len(string)//2:])

def main() -> tuple[int, int]:
    data = get_data(day=3, year=2022).split()
    ans1 = sum(map(stringPriority, data))
    ans2 = sum(starmap(groupPriority, zip(data[::3], data[1::3], data[2::3])))
    return ans1, ans2

if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")