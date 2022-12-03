from aocd import get_data, submit
from typing import Iterable

def itemPriority(char: str) -> int:
    return 1 + ord(char) - ord('a') if char.islower() else 27 + ord(char) - ord('A')

def groupPriority(*string_list: Iterable[str]) -> int:
    return itemPriority(set.intersection(*(set(x) for x in string_list)).pop())

def main() -> tuple[int, int]:
    data = get_data(day=3, year=2022).split()
    ans1 = sum(map(lambda x: groupPriority(x[:len(x)//2], x[len(x)//2:]), data))
    ans2 = sum(map(lambda x: groupPriority(*x), zip(data[::3], data[1::3], data[2::3])))
    return ans1, ans2

if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")