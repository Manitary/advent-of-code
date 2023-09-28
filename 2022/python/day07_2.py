"""Solve Advent of Code Day 7 Year 2022."""

from __future__ import annotations

from abc import ABC
from bisect import insort
from dataclasses import dataclass, field

from aocd import get_data, submit

SMALL_SIZE = 100000
TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000


@dataclass
class Item(ABC):
    """Item(name, parent) -> Item

    Create a new item object with the given name and parent.
    """

    name: str
    parent: Item | None = None

    @property
    def path(self) -> str:
        """Return the full path of the item."""
        ans = self.name
        current = self
        while current := current.parent:
            ans = f"{current.name}/{ans}"
        return ans


@dataclass
class File(Item):
    """File(name, parent, size=0) -> File

    Create a new item object with the given size. Its parent can only be a Folder object.
    """

    size: int = 0
    parent: Folder | None = None


@dataclass
class Folder(Item):
    """Folder(name, parent, subfolders=[], files=[]) -> Folder

    Create a new folder object, containing the given lists of subfolders and files.
    Its parent can only be a Folder object.
    """

    parent: Folder | None = None
    subfolders: list[Folder] = field(default_factory=list)
    files: list[File] = field(default_factory=list)

    @property
    def size(self) -> int:
        """Return the sum of all files and subfolders contained in the folder."""
        subfolders_size = sum(folder.size for folder in self.subfolders)
        files_size = sum(file_.size for file_ in self.files)
        return subfolders_size + files_size

    def create_subfolder(self, folder_name: str) -> None:
        """Create a subfolder with the given name, if one does not already exist."""
        if all(subfolder.name != folder_name for subfolder in self.subfolders):
            insort(
                self.subfolders,
                Folder(name=folder_name, parent=self),
                key=lambda x: x.name,
            )

    def create_file(self, file_name: str, size: int = 0) -> None:
        """Create a file with the given name and size, if one does not already exist."""
        if all(file_.name != file_name for file_ in self.files):
            insort(
                self.files,
                File(name=file_name, parent=self, size=size),
                key=lambda x: x.name,
            )

    def structure(self, level: int = 0) -> str:
        """Return a string describing the folder structure."""
        ans = f"{'  '*level}- {self.name} (dir)"
        for folder in self.subfolders:
            ans += f"\n{folder.structure(level=level+1)}"
        for file_ in self.files:
            ans += f"\n{'  '*(level+1)}- {file_.name} (file, size={file_.size})"
        return ans


def build_folder_structure(commands: list[str], root_name: str = "/") -> Folder:
    """Return the root folder of the filesystem traversed by the given list of commands."""
    root = Folder(name=root_name)
    current = root
    for command in commands:
        match command.split():
            case ["$", "cd", "/"]:
                current = root
            case ["$", "cd", ".."]:
                current = current.parent or current
            case ["$", "cd", folder_name]:
                current.create_subfolder(folder_name=folder_name)
                current = next(
                    subfolder
                    for subfolder in current.subfolders
                    if subfolder.name == folder_name
                )
            case ["$", "ls"]:
                continue
            case ["dir", folder_name]:
                current.create_subfolder(folder_name=folder_name)
            case [file_size, file_name]:
                current.create_file(file_name=file_name, size=int(file_size))
            case _:
                raise ValueError("Unmatched case")

    return root


def main() -> tuple[int, int]:
    """Return the answers to part 1 and part 2."""
    data = get_data(day=7, year=2022).split("\n")
    home = build_folder_structure(data)
    needed = home.size - TOTAL_SPACE + SPACE_NEEDED
    part1, part2 = 0, TOTAL_SPACE
    queue = [home]
    while queue:
        current = queue.pop(0)
        if current.size <= SMALL_SIZE:
            part1 += current.size
        if current.size >= needed:
            part2 = min(part2, current.size)
        queue.extend(current.subfolders)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=7, year=2022)
    submit(ans2, part="b", day=7, year=2022)
