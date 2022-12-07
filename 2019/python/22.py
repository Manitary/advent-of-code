from aocd import get_data, submit
from itertools import count

DAY = 22
YEAR = 2019

data = get_data(day=DAY, year=YEAR)


class Deck:
    def __init__(self, size: int = 0):
        self.size = size
        self.top = 0
        self.step = 1

    def shuffle(self, instruction: list[str]):
        match instruction:
            case ["cut", x]:
                self.top = (self.top + self.step * int(x)) % self.size
            case ["deal", "into", *_]:
                self.top = (self.top - self.step) % self.size
                self.step = (-self.step) % self.size
            case ["deal", "with", "increment", x]:
                self.step = (self.step * pow(int(x), -1, self.size)) % self.size

    def bigShuffle(self, instructions: list[list[str]]):
        for instruction in instructions:
            self.shuffle(instruction)


data = [row.split() for row in data.split("\n")]

deck = Deck(10007)
deck.bigShuffle(data)
target = 2019
card = deck.top
for i in count():
    if card == 2019:
        ans1 = i
        break
    card = (card + deck.step) % deck.size

N = 101741582076661
M = 119315717514047
deck = Deck(M)
deck.bigShuffle(data)

"""
After each shuffle:
* top is increased by step times a constant coefficient
* step is multiplied by a constant coefficient
Starting with top=0 and step=1, the coefficients are the values of top and step after the first shuffle
"""
new_top = deck.top * (pow(deck.step, N, M) - 1) * pow(deck.step - 1, -1, M)
new_step = pow(deck.step, N, M)
ans2 = new_top
for _ in range(2020):
    ans2 = (ans2 + new_step) % M

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
