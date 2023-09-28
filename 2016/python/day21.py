from aocd import get_data, submit

DAY = 21
YEAR = 2016

PASSWORD_1 = "abcdefgh"
PASSWORD_2 = "fbgdceah"


def swap_position(string: list[str], index1: int, index2: int) -> list[str]:
    tmp = string[index2]
    string[index2] = string[index1]
    string[index1] = tmp
    return string


def swap_letter(string: list[str], char1: str, char2: str) -> list[str]:
    i1, i2 = string.index(char1), string.index(char2)
    string[i1], string[i2] = char2, char1
    return string


def rotate_step(string: list[str], direction: str, step: int) -> list[str]:
    step %= len(string)
    if direction == "right":
        string = string[-step:] + string[:-step]
    elif direction == "left":
        string = string[step:] + string[:step]
    return string


def rotate_letter(
    string: list[str], letter: str, direction: str = "right"
) -> list[str]:
    step = string.index(letter)
    step += 2 if step >= 4 else 1
    return rotate_step(string, direction, step)


def reverse_position(string: list[str], index1: int, index2: int) -> list[str]:
    return (
        string[:index1]
        + string[index2 - len(string) : index1 - len(string) - 1 : -1]
        + string[index2 + 1 :]
    )


def move_position(string: list[str], index1: int, index2: int) -> list[str]:
    string.insert(index2, string.pop(index1))
    return string


def execute(string: list[str], operation: list[str], undo: bool = False) -> list[str]:
    match operation:
        case ["swap", "position", x, "with", "position", y]:
            return swap_position(string, int(x), int(y))
        case ["swap", "letter", x, "with", "letter", y]:
            return swap_letter(string, x, y)
        case ["rotate", direction, x, ("steps" | "step")]:
            if undo:
                return rotate_step(
                    string, "right" if direction == "left" else "left", int(x)
                )
            return rotate_step(string, direction, int(x))
        case ["rotate", "based", "on", *rest]:
            if undo:
                current = string.index(rest[-1])
                for i in range(len(string)):
                    if (2 * i + (2 if i >= 4 else 1)) % len(string) != current:
                        continue
                    if i >= current:
                        return rotate_step(string, "right", i - current)
                    return rotate_step(string, "left", current - i)
            return rotate_letter(string, rest[-1])
        case ["reverse", "positions", x, "through", y]:
            return reverse_position(string, int(x), int(y))
        case ["move", "position", x, "to", "position", y]:
            if undo:
                return move_position(string, int(y), int(x))
            return move_position(string, int(x), int(y))
        case _:
            raise ValueError("Invalid operation")


def scramble(data: list[list[str]], string: str) -> str:
    list_string = list(string)
    for row in data:
        list_string = execute(list_string, row)
    return "".join(list_string)


def unscramble(data: list[list[str]], string: str) -> str:
    list_string = list(string)
    for row in data[::-1]:
        list_string = execute(list_string, row, undo=True)
    return "".join(list_string)


def main() -> tuple[str, str]:
    data = get_data(day=DAY, year=YEAR)
    data = [row.split() for row in data.split("\n")]
    part1 = scramble(data, PASSWORD_1)
    part2 = unscramble(data, PASSWORD_2)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
