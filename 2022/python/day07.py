"""Solve Advent of Code Day 7 Year 2022."""

from aocd import get_data, submit

ROOT_FOLDER = 'home'
SMALL_SIZE = 100000
TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000

def path_level_to_string(path: list[str], level: int) -> str:
    """Return the full path up to the given level."""
    return f"{'/'.join(path[:level + 1])}/"

def path_to_string(path: list[str], item: str) -> str:
    """Return the full path of an item (file or folder) inside the given path."""
    return f"{'/'.join(path)}/{item}/"

def get_folder_structure(commands: list[str]) -> dict[str, int]:
    """
    Given a list of commands to traverse the filesystem,
    return a dictionary of folder paths and their size.
    """
    current_path = [ROOT_FOLDER]
    directories = {f"{ROOT_FOLDER}/": 0}
    for command in commands:
        match command.split():
            case ['$', 'cd', '/']:
                current_path = current_path[:1]
            case ['$', 'cd', '..']:
                current_path.pop()
            case ['$', 'cd', folder_name]:
                if path_to_string(current_path, folder_name) in directories:
                    current_path.append(folder_name)
            case ['$', 'ls']:
                continue
            case ['dir', folder_name]:
                directories[path_to_string(current_path, folder_name)] = 0
            case [file_size, _]:
                for i, _ in enumerate(current_path):
                    directories[path_level_to_string(current_path, i)] += int(file_size)

    return directories

def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=7, year=2022).split('\n')
    directories = get_folder_structure(data)
    part1 = sum(size for size in directories.values() if size <= SMALL_SIZE)
    needed = directories[f"{ROOT_FOLDER}/"] - TOTAL_SPACE + SPACE_NEEDED
    part2 = min(x for x in directories.values() if x >= needed)

    return part1, part2

if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
