from aocd import get_data, submit

DAY = 21
YEAR = 2016

data = get_data(day=DAY, year=YEAR)

data = [row.split() for row in data.split("\n")]


def swapPosition(string: list[str], index1: int, index2: int):
    tmp = string[index2]
    string[index2] = string[index1]
    string[index1] = tmp
    return string


def swapLetter(string: list[str], char1: str, char2: str):
    i1, i2 = string.index(char1), string.index(char2)
    string[i1], string[i2] = char2, char1
    return string


def rotateStep(string: list[str], direction: str, step: int):
    step %= len(string)
    if direction == "right":
        string = string[-step:] + string[:-step]
    elif direction == "left":
        string = string[step:] + string[:step]
    return string


def rotateLetter(string: list[str], letter: str, direction: str = "right"):
    step = string.index(letter)
    step += 2 if step >= 4 else 1
    return rotateStep(string, direction, step)


def reversePosition(string: list[str], index1: int, index2: int):
    return (
        string[:index1]
        + string[index2 - len(string) : index1 - len(string) - 1 : -1]
        + string[index2 + 1 :]
    )


def movePosition(string: list[str], index1: int, index2: int):
    string.insert(index2, string.pop(index1))
    return string


def execute(string: list[str], operation: list[str], undo: bool = False):
    match operation:
        case ["swap", "position", x, "with", "position", y]:
            return swapPosition(string, int(x), int(y))
        case ["swap", "letter", x, "with", "letter", y]:
            return swapLetter(string, x, y)
        case ["rotate", direction, x, ("steps" | "step")]:
            if undo:
                return rotateStep(
                    string, "right" if direction == "left" else "left", int(x)
                )
            return rotateStep(string, direction, int(x))
        case ["rotate", "based", "on", *rest]:
            if undo:
                current = string.index(rest[-1])
                for i in range(len(string)):
                    if (2 * i + (2 if i >= 4 else 1)) % len(string) == current:
                        if i >= current:
                            return rotateStep(string, "right", i - current)
                        else:
                            return rotateStep(string, "left", current - i)
            return rotateLetter(string, rest[-1])
        case ["reverse", "positions", x, "through", y]:
            return reversePosition(string, int(x), int(y))
        case ["move", "position", x, "to", "position", y]:
            if undo:
                return movePosition(string, int(y), int(x))
            return movePosition(string, int(x), int(y))


def scramble(string: str):
    string = list(string)
    for row in data:
        print(string, row)
        string = execute(string, row)
    return "".join(string)


def unscramble(string: str):
    string = list(string)
    for row in data[::-1]:
        print(string, row)
        string = execute(string, row, undo=True)
    return "".join(string)


password = "abcdefgh"
ans1 = scramble(password)

password = "fbgdceah"
ans2 = unscramble(password)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
