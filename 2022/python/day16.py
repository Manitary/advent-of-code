import re
from collections import defaultdict
from typing import NamedTuple

from aocd import get_data, submit

DAY = 16
YEAR = 2022

EDGE_RE = re.compile(r"\d+|[A-Z]{2}")

type Tunnel = tuple[str, str]


class Valve(NamedTuple):
    rate: int
    exits: list[str]


def parse_valve(line: str) -> tuple[str, Valve]:
    source, rate, *exits = EDGE_RE.findall(line)
    return source, Valve(int(rate), exits)


def parse_data(lines: list[str]) -> dict[str, Valve]:
    return dict(map(parse_valve, lines))


def find_distances(rooms: dict[str, Valve], key_rooms: set[str]) -> dict[Tunnel, int]:
    """Return a map of distances key_room -> room."""
    distances: dict[tuple[str, str], int] = {}
    for start_room in key_rooms:
        # BFS from start_room
        queue: list[tuple[str, int]] = [(start_room, 1)]
        while queue:
            curr, d = queue.pop(0)
            for new in rooms[curr].exits:
                if (start_room, new) in distances:
                    continue
                distances[start_room, new] = d
                queue.append((new, d + 1))

    return distances


def find_best_total_flow(
    rooms: dict[str, Valve],
    distances: dict[Tunnel, int],
    start: str = "AA",
    time: int = 30,
) -> int:
    """Return the best total flow, given the starting point and time left.

    (The valve at the starting node has already been opened)"""
    return max(
        (
            valve.rate * time_left
            + find_best_total_flow(
                {k: v for k, v in rooms.items() if k != start},
                distances,
                target,
                time_left,
            )
            for target, valve in rooms.items()
            if target != start
            and (time_left := time - distances[start, target] - 1) > 0
        ),
        default=0,
    )


def main() -> tuple[int, int]:
    data = get_data(day=16, year=2022)
    rooms = parse_data(data.splitlines())
    key_rooms = {l: valve for l, valve in rooms.items() if valve.rate or l == "AA"}
    distances = find_distances(rooms, set(key_rooms))

    part1 = find_best_total_flow(key_rooms, distances)

    endpoints: dict[frozenset[str], int] = defaultdict(lambda: 0)

    def find_and_record(
        start: str = "AA",
        cur_flow: int = 0,
        time: int = 26,
        seen: set[str] | None = None,
    ) -> int:
        seen = seen | {start} if seen else {start}

        to_record = frozenset(seen - {"AA"})
        endpoints[to_record] = max(endpoints[to_record], cur_flow)

        return max(
            (
                valve.rate * time_left
                + find_and_record(
                    target,
                    cur_flow + valve.rate * time_left,
                    time_left,
                    seen,
                )
                for target, valve in key_rooms.items()
                if target not in seen
                and (time_left := time - distances[start, target] - 1) > 0
            ),
            default=0,
        )

    # Find all the best 26 minute flow rates
    find_and_record()

    # Fill in all missing subsets of rooms
    def fill_in_endpoints(cur: frozenset[str]) -> int:
        if cur not in endpoints:
            endpoints[cur] = max(fill_in_endpoints(cur - {e}) for e in cur)
        return endpoints[cur]

    fill_in_endpoints(frozenset(key_rooms.keys() - {"AA"}))

    # Check all the possible assignments of rooms
    part2 = max(
        flow + endpoints[frozenset(key_rooms.keys() - {"AA"} - human_work)]
        for human_work, flow in endpoints.items()
    )

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a")
    submit(ans2, part="b")
