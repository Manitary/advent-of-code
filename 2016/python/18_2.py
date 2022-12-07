from aocd import get_data, submit
import numpy as np

DAY = 18
YEAR = 2016


class Game(object):
    def __init__(self, data):
        self._state = self.parse(data)
        self._length = self.state.shape[0]

    @property
    def state(self):
        return self._state[1:-1]

    @staticmethod
    def parse(data):
        size = len(data)
        state = np.zeros(size + 2, dtype=np.uint8)
        for i, char in enumerate(data):
            state[i + 1] = 1 if char == "^" else 0
        return state

    def newRow(self):
        return np.bitwise_xor(self._state[:-2], self._state[2:])

    def nextState(self):
        new = self.newRow()
        self._state[...] = 0
        self._state[1:-1] = new

    def numSafe(self):
        return self._length - np.sum(self.state)


def solve():
    data = get_data(day=DAY, year=YEAR)
    game = Game(data)
    n1, n2 = 40, 400000
    ans1, ans2 = None, game.numSafe()
    for i in range(n2 - 1):
        game.nextState()
        ans2 += game.numSafe()
        if i == n1 - 2:
            ans1 = ans2

    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)


if __name__ == "__main__":
    solve()
