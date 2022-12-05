from aocd import get_data, submit

def main() -> tuple[int, int]:
    cargo, instructions = (x.split('\n') for x in get_data(day=5, year=2022).split('\n\n'))
    cargo_size = int(cargo[-1].split()[-1])
    stacks = [[] for _ in range(cargo_size)]
    for row in cargo[-2::-1]:
        crates = row[1::4]
        for i, crate in enumerate(crates):
            if crate != ' ':
                stacks[i].append(crate)
    stacks2 = [s[:] for s in stacks]
    for instruction in instructions:
        num, start, end = map(int, instruction.split()[1::2])
        # Part 1
        for _ in range(num):
            stacks[end-1].append(stacks[start-1].pop())
        # Part 2
        stacks2[end-1].extend(stacks2[start-1][-num:])
        del stacks2[start-1][-num:]

    ans1 = ''.join(s[-1] for s in stacks)
    ans2 = ''.join(s[-1] for s in stacks2)
    return ans1, ans2

if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")