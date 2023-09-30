from aocd import get_data, submit

DAY = 14
YEAR = 2018


def main() -> tuple[str, int]:
    data = get_data(day=DAY, year=YEAR)
    score = [3, 7]
    to_check = tuple(map(int, list(data)))
    elf_1, elf_2 = 0, 1
    idx, pos = 0, 0
    part1, part2 = 0, 0
    while not (part1 and part2):
        score.extend(map(int, list(str(score[elf_1] + score[elf_2]))))
        elf_1 = (elf_1 + score[elf_1] + 1) % len(score)
        elf_2 = (elf_2 + score[elf_2] + 1) % len(score)
        if (not part1) and len(score) > int(data) + 10:
            part1 = "".join(map(str, score[int(data) : int(data) + 10]))
        while idx + pos < len(score):
            if to_check[pos] != score[idx + pos]:
                pos = 0
                idx += 1
                continue
            if pos == len(data) - 1:
                part2 = idx
                break
            pos += 1
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
