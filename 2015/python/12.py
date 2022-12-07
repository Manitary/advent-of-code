from aocd import get_data, submit
import json

DAY = 12
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

data = json.JSONDecoder().decode(data)


def sumAll(elt, excluded=None):
    if isinstance(elt, int):
        return elt
    if isinstance(elt, str):
        return 0
    ans = 0
    for k in elt:
        if isinstance(elt, list):
            ans += sumAll(k, excluded)
        elif excluded and elt[k] in excluded:
            ans = 0
            break
        else:
            ans += sumAll(elt[k], excluded)
    return ans


ans1 = sumAll(data)
ans2 = sumAll(data, excluded=["red"])

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
