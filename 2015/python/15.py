from aocd import get_data, submit
from re import findall, compile
import numpy as np

DAY = 15
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split("\n")

pattern = r"-?\d+"
compile(pattern)
ingredients = np.matrix(
    [np.array(findall(pattern, ingredient), int) for ingredient in data]
)


def bestRecipe(teaspoons=100, cal=500):
    ans1, ans2 = 0, 0
    for recipe in (
        np.array([a, b, c, teaspoons - a - b - c])
        for a in range(teaspoons)
        for b in range(teaspoons - a)
        for c in range(teaspoons - a - b)
    ):
        m = (recipe * ingredients).clip(min=0)
        score = np.prod(m[0, :-1])
        ans1 = max(ans1, score)
        if m[0, -1] == cal:
            ans2 = max(ans2, score)
    return ans1, ans2


ans1, ans2 = bestRecipe()

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
