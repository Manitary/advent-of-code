from aocd import get_data, submit
from re import findall, compile
DAY = 14
YEAR = 2015

data = get_data(day=DAY, year=YEAR).split("\n")
TIME_LIMIT = 2503

pattern = compile(r"\d+")

def pos(reindeer, elapsed):
    s, ft, rt = reindeer['speed'], reindeer['max_time_flying'], reindeer['max_time_resting']
    return s * (elapsed // (ft + rt) * ft + min(ft, elapsed % (ft + rt)))

reindeers = {}
for i, row in enumerate(data):
    s, ft, rt = map(int, tuple(findall(pattern, row)))
    reindeers[i] = {
        'speed': s,
        'max_time_flying': ft,
        'max_time_resting': rt,
        'time_flying': 0,
        'time_resting': 0,
    }

ans1 = max(iter(pos(reindeer, TIME_LIMIT) for _, reindeer in reindeers.items()))

distance = [0 for _ in range(len(reindeers))]
score = [0 for _ in range(len(reindeers))]
for t in range(TIME_LIMIT):
    for i, r in reindeers.items():
        if r['time_flying'] < r['max_time_flying']:
            r['time_flying'] += 1
            distance[i] += r['speed']
        else:
            r['time_resting'] += 1
            if r['time_resting'] == r['max_time_resting']:
                r['time_flying'] = 0
                r['time_resting'] = 0
    best = max(distance)
    for i, d in enumerate(distance):
        if d == best:
            score[i] += 1

ans2 = max(score)

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)