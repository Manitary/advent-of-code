import numpy as np
from aocd import get_data, submit
from numpy.typing import NDArray

DAY = 18
YEAR = 2016

Grid = NDArray[np.uint8]


class Game:
    def __init__(self, data: str) -> None:
        self._state = self.parse(data)
        self._length = self.state.shape[0]

    @property
    def state(self) -> Grid:
        return self._state[1:-1]

    @staticmethod
    def parse(data: str) -> Grid:
        size = len(data)
        state = np.zeros(size + 2, dtype=np.uint8)
        for i, char in enumerate(data):
            state[i + 1] = 1 if char == "^" else 0
        return state

    def new_row(self) -> Grid:
        return np.bitwise_xor(self._state[:-2], self._state[2:])

    def next_state(self) -> None:
        new = self.new_row()
        self._state[...] = 0
        self._state[1:-1] = new

    def num_safe(self) -> int:
        return self._length - np.sum(self.state)


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)
    game = Game(data)
    n1, n2 = 40, 400000
    part1, part2 = 0, game.num_safe()
    for i in range(n2 - 1):
        game.next_state()
        part2 += game.num_safe()
        if i == n1 - 2:
            part1 = part2
    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
