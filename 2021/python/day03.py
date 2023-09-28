"""Solve Advent of Code Day 1 Year 2021."""

from typing import Callable, Iterable

from aocd import get_data, submit


def bit_criterion(numbers: list[str], index: int, priority: int = 1) -> str:
    """
    Return the bit criterion for the given bit index.

        priority:
            1: return the most common bit, 1 if tied
            0: return the least common bit, 0 if tied
    """
    ones = sum(number[index] == "1" for number in numbers)
    val = priority if ones >= len(numbers) / 2 else 1 - priority
    return str(val)


def bit_filter(
    numbers: list[str], index: int, priority: int = 1
) -> Callable[[str], bool]:
    """Return a function that checks whether an input number satisfies the bit filter."""

    def is_valid_number(number: str) -> bool:
        """Return whether the given number satisfies the bit filter."""
        return number[index] == bit_criterion(
            numbers=numbers, index=index, priority=priority
        )

    return is_valid_number


def binary_to_int(bits: Iterable[str]) -> int:
    """Return the integer with binary representation given by bits."""
    return int("".join(bits), 2)


def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=3, year=2021).split()
    n_bits = len(data[0])
    mask = 2**n_bits - 1
    gamma_rate = binary_to_int(bit_criterion(data, i) for i in range(n_bits))
    epsilon_rate = ~gamma_rate & mask

    part1 = gamma_rate * epsilon_rate

    oxy = co2 = data
    for i in range(n_bits):
        oxy: list[str] = list(filter(bit_filter(oxy, i), oxy)) if len(oxy) > 1 else oxy
        co2: list[str] = (
            list(filter(bit_filter(co2, i, 0), co2)) if len(co2) > 1 else co2
        )

    part2 = binary_to_int(oxy) * binary_to_int(co2)

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
