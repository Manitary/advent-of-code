import functools
from collections import Counter
from functools import cache
from typing import Callable

from aocd import get_data, submit

DAY = 7
YEAR = 2023


@cache
def hand_rank_1(hand: str) -> list[int]:
    return sorted(Counter(hand).values(), reverse=True)


@cache
def card_score_1(c: str) -> int:
    if c == "T":
        return 10
    if c == "J":
        return 11
    if c == "Q":
        return 12
    if c == "K":
        return 13
    if c == "A":
        return 14
    return int(c)


@cache
def hand_rank_2(hand: str) -> list[int]:
    counter = Counter(hand)
    jokers = counter.pop("J", 0)
    if not counter:
        return [5]
    if jokers:
        counter[counter.most_common(1)[0][0]] += jokers
    return sorted(counter.values(), reverse=True)


@cache
def card_score_2(c: str) -> int:
    if c == "J":
        return 1
    return card_score_1(c)


def calculate_score(
    hands_and_bids: list[list[str]],
    scoring_method: Callable[[str], tuple[list[int], tuple[int, ...]]],
) -> int:
    sorted_input = sorted(hands_and_bids, key=lambda row: scoring_method(row[0]))
    return sum(i * int(row[1]) for i, row in enumerate(sorted_input, 1))


@cache
def score(
    hand: str,
    rank_score: Callable[[str], list[int]],
    card_score: Callable[[str], int],
) -> tuple[list[int], tuple[int, ...]]:
    return rank_score(hand), tuple(card_score(c) for c in hand)


score_1 = functools.partial(score, rank_score=hand_rank_1, card_score=card_score_1)
score_2 = functools.partial(score, rank_score=hand_rank_2, card_score=card_score_2)


def main() -> tuple[int, int]:
    data = [row.split() for row in get_data(day=DAY, year=YEAR).splitlines()]
    part1 = calculate_score(data, score_1)
    part2 = calculate_score(data, score_2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
