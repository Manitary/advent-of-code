from advent_of_code_ocr import convert_6
from aocd import get_data, submit
from intcode import Robot

DAY = 11
YEAR = 2019


def main() -> tuple[int, str]:
    data = get_data(day=DAY, year=YEAR)

    painter = Robot(program=data)
    painter.move()
    part1 = len(painter.visited)

    painter = Robot(program=data, starting_panel=1)
    painter.move()

    xs = tuple(t[0] for t, val in painter.visited.items() if val == 1)
    ys = tuple(t[1] for t, val in painter.visited.items() if val == 1)

    part2 = convert_6(
        "\n".join(
            [
                "".join(
                    [
                        "#" if painter.visited[(x, y)] == 1 else "."
                        for x in range(min(xs), max(xs) + 1)
                    ]
                )
                for y in range(max(ys), min(ys) - 1, -1)
            ]
        )
    )
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
