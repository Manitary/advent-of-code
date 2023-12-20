from __future__ import annotations

import copy
import enum
import itertools
import math
from collections import Counter
from typing import override

from aocd import get_data, submit

DAY = 20
YEAR = 2023


class Status(enum.IntEnum):
    OFF = 0
    ON = 1


class Pulse(enum.IntEnum):
    LOW = 0
    HIGH = 1


class Module:
    __slots__ = "label", "children", "queue", "log"

    def __init__(self, label: str) -> None:
        self.label = label
        self.children: list[Module] = []
        self.queue: list[tuple[Module, Pulse]] = []
        self.log = {p: 0 for p in Pulse}

    def add_parent(self, parent: Module) -> None:
        pass

    def add_child(self, child: Module) -> None:
        if child in self.children:
            raise ValueError("Module is already a child")
        self.children.append(child)
        child.add_parent(self)

    def push(self, module: Module, pulse: Pulse) -> None:
        self.queue.append((module, pulse))

    def send(self, pulse: Pulse) -> None:
        for child in self.children:
            child.push(self, pulse)

    def activate(self) -> list[Module]:
        raise NotImplementedError()

    def process_queue(self) -> None:
        while self.queue:
            self.process_pulse(self.queue.pop(0)[1])

    def process_pulse(self, pulse: Pulse) -> None:
        raise NotImplementedError()


class Broadcaster(Module):
    __slots__ = ("parents",)

    def __init__(self, label: str) -> None:
        super().__init__(label)
        self.parents: set[Module] = set()

    @override
    def activate(self) -> list[Module]:
        self.process_queue()
        return self.children

    @override
    def process_pulse(self, pulse: Pulse) -> None:
        self.send(pulse)
        self.log[pulse] += len(self.children)

    @override
    def add_parent(self, parent: Module) -> None:
        self.parents.add(parent)


class FlipFlop(Module):
    __slots__ = ("status",)

    def __init__(self, label: str) -> None:
        super().__init__(label)
        self.status = Status.OFF

    @override
    def activate(self) -> list[Module]:
        inactive = all(p == Pulse.HIGH for _, p in self.queue)
        self.process_queue()
        if inactive:
            return []
        return self.children

    @override
    def process_pulse(self, pulse: Pulse) -> None:
        if pulse == Pulse.HIGH:
            return
        self.status = Status(1 - self.status)
        to_send = Pulse(self.status)
        self.send(to_send)
        self.log[to_send] += len(self.children)


class Conjunction(Module):
    __slots__ = "history", "_to_send"

    def __init__(self, label: str) -> None:
        super().__init__(label)
        self._to_send = Pulse.LOW
        self.history: dict[Module, Pulse] = {}

    @override
    def add_parent(self, parent: Module) -> None:
        self.history[parent] = Pulse.LOW

    @override
    def activate(self) -> list[Module]:
        self.update_history()
        self.process_queue()
        return self.children

    @override
    def process_pulse(self, pulse: Pulse) -> None:
        self.send(self._to_send)
        self.log[self._to_send] += len(self.children)

    def update_history(self) -> None:
        for module, pulse in self.queue:
            self.history[module] = pulse
        self._to_send = Pulse(1 - all(self.history.values()))

    @property
    def last_pulse(self) -> Pulse:
        return self._to_send


def parse_input(data: list[str]) -> dict[str, Module]:
    modules: dict[str, Module] = {}
    for row in data:
        label = row.split()[0]
        if label.startswith("%"):
            modules[label[1:]] = FlipFlop(label[1:])
        elif label.startswith("&"):
            modules[label[1:]] = Conjunction(label[1:])
        else:
            modules[label] = Broadcaster(label)

    for row in data:
        l, t = row.split(" -> ")
        l = l[1:] if l[0] in "&%" else l
        for x in t.split(", "):
            if x not in modules:
                modules[x] = Broadcaster(x)
            modules[l].add_child(modules[x])

    modules["button"] = Broadcaster("button")
    modules["button"].add_child(modules["broadcaster"])

    return modules


def part_1(modules: dict[str, Module]) -> int:
    origin = Module("")
    for _ in range(1000):
        modules["button"].push(origin, Pulse.LOW)
        queue = [modules["button"]]
        while queue:
            new_queue = queue.pop(0).activate()
            for child in new_queue:
                if child not in queue:
                    queue.append(child)

    counts: Counter[Pulse] = Counter()
    for module in modules.values():
        counts.update(module.log)

    return math.prod(counts.values())


def part_2(modules: dict[str, Module]) -> int:
    target = modules["rx"]
    assert isinstance(target, Broadcaster)
    assert len(target.parents) == 1
    parent = tuple(target.parents)[0]
    assert isinstance(parent, Conjunction)
    sources = tuple(parent.history.keys())
    assert all(isinstance(source, Conjunction) for source in sources)
    # The target has a unique Conjunction parent (parent),
    # which in turn only has Conjunction parents (sources).
    # The target receives a low pulse from parent when parent receives all high pulses from sources.
    # We can verify that each source lies in a separate subsection of the flow graph,
    # so we can calculate the frequency of them sending a high pulse independently.

    source_cycles: dict[Module, int] = {}
    origin = Module("")
    for cycle in itertools.count(start=1):
        modules["button"].push(origin, Pulse.LOW)
        queue = [modules["button"]]
        while queue:
            curr = queue.pop(0)
            new_queue = curr.activate()
            for child in new_queue:
                if child not in queue:
                    queue.append(child)
            if (
                curr in sources
                and curr not in source_cycles
                and isinstance(curr, Conjunction)
                and curr.last_pulse == Pulse.HIGH
            ):
                source_cycles[curr] = cycle
                if len(source_cycles) == len(sources):
                    return math.lcm(*source_cycles.values())

    raise ValueError("Invalid input")


def main() -> tuple[int, int]:
    data = get_data(day=DAY, year=YEAR)

    modules = parse_input(data.splitlines())
    part1 = part_1(copy.deepcopy(modules))
    part2 = part_2(copy.deepcopy(modules))

    return part1, part2


if __name__ == "__main__":
    ans1, ans2 = main()
    submit(ans1, part="a", day=DAY, year=YEAR)
    submit(ans2, part="b", day=DAY, year=YEAR)
