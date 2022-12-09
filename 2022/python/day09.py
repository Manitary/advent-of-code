"""Solve Advent of Code Day 9 Year 2022."""

from aocd import get_data, submit


def move_coords(coords: tuple[int, int], direction: str) -> tuple[int, int]:
    """Return the new coordinates after moving in the given direction.

    direction:
        "U", "D", "L", "R"
    """
    x, y = coords
    if direction == "U":
        return (x, y + 1)
    if direction == "D":
        return (x, y - 1)
    if direction == "L":
        return (x - 1, y)
    if direction == "R":
        return (x + 1, y)
    raise ValueError("Invalid direction.")


def adjust_coordinate(head: int, tail: int) -> int:
    """Adjust the coordinate of the tail by moving it closer to the head."""
    if head == tail:
        return tail
    if head > tail:
        return tail + 1
    if head < tail:
        return tail - 1
    raise RuntimeError("All comparisons failed: something has gone horribly wrong")


def follow(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    """Return the new position of the tail after following the head."""
    x_tail, y_tail = tail
    x_head, y_head = head
    if abs(x_tail - x_head) <= 1 and abs(y_tail - y_head) <= 1:
        return tail
    x_tail = adjust_coordinate(x_head, x_tail)
    y_tail = adjust_coordinate(y_head, y_tail)
    return (x_tail, y_tail)


def get_trail(rope_length: int, moves: list[str]) -> set[tuple[int, int]]:
    """Return the set of coordinates visited by the tail end of the rope after the given moves."""
    rope = [(0, 0)] * rope_length
    visited = set()
    for move in moves:
        direction, num_moves = move.split()
        for _ in range(int(num_moves)):
            for i, _ in enumerate(rope):
                if i == 0:
                    rope[i] = move_coords(rope[i], direction)
                else:
                    rope[i] = follow(rope[i - 1], rope[i])
            visited.add(rope[-1])
    return visited


def main() -> tuple[int, int]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=9, year=2022).split("\n")
    part1 = len(get_trail(2, data))
    part2 = len(get_trail(10, data))
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
