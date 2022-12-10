"""Solve Advent of Code Day 10 Year 2022."""

from aocd import get_data, submit
from advent_of_code_ocr import convert_array_6


class MatrixPointer:
    """A two-dimensional pointer."""

    def __init__(self, rows: int, cols: int) -> None:
        """Create a MatrixPointer with the given bounds.

        Args:
            rows: total number of rows.
            cols: total number of columns."""
        self._max_row = rows
        self._max_col = cols
        self._row = 0
        self._col = 0

    @property
    def row(self) -> int:
        """Return the current row."""
        return self._row

    @property
    def col(self) -> int:
        """Return the current column."""
        return self._col

    def increase(self) -> None:
        """Advance the pointer.

        Advance the pointer by one (left to right, top to bottom),
        reset it to position (0, 0) when reaching the bound."""
        self._col += 1
        if self._col == self._max_col:
            self._col = 0
            self._row += 1
            if self._row == self._max_row:
                self._row, self._col = 0, 0


class CRT:
    """A CRT monitor."""

    def __init__(self, width: int, height: int) -> None:
        """Create a monitor with the given sizes."""
        self._width = width
        self._height = height
        self._register = 1
        self._signals = []
        self._pointer = MatrixPointer(rows=height, cols=width)
        self._screen = [[0] * width for _ in range(height)]

    @property
    def screen(self) -> list[list[int]]:
        """Return the contents of the screen."""
        return self._screen

    def __str__(self) -> str:
        return "\n".join(
            "".join("#" if tile else " " for tile in row) for row in self._screen
        )

    def get_signal_strength(self, cycle: int) -> int:
        """Return the signal strength at the given cycle."""
        return cycle * self._signals[cycle - 1]

    def execute(self, instruction: str) -> None:
        """Execute the given instruction and update the screen."""
        match instruction.split():
            case ["noop"]:
                self.update_crt()
                self.update_signals()
            case ["addx", num]:
                for _ in range(2):
                    self.update_crt()
                    self.update_signals()
                self._register += int(num)

    def update_signals(self) -> None:
        """Update the list of sent signals with the current value of the register."""
        self._signals.append(self._register)

    def update_crt(self) -> None:
        """Update the screen at the location of the pointer."""
        row, col = self._pointer.row, self._pointer.col
        self._screen[row][col] |= abs(self._register - col) <= 1
        self._pointer.increase()


def main() -> tuple[int, str]:
    """Return the solution to part 1 and part 2."""
    data = get_data(day=10, year=2022).split("\n")
    monitor = CRT(width=40, height=6)
    for instruction in data:
        monitor.execute(instruction)
    part1 = sum(monitor.get_signal_strength(i) for i in range(20, 221, 40))
    part2 = convert_array_6(monitor.screen, fill_pixel=1, empty_pixel=0)
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
