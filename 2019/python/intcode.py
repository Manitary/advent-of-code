from collections import defaultdict, deque
from copy import deepcopy
from typing import Generator

# Modes
POSITION = 0
IMMEDIATE = 1
RELATIVE = 2

# Opcodes
ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
BASE_ADJUST = 9
HALT = 99

# Role of the parameters for each opcode
READ = 0
WRITE = 1
OPCODES: dict[int, tuple[int, ...]] = {
    ADD: (READ, READ, WRITE),
    MULT: (READ, READ, WRITE),
    INPUT: (WRITE,),
    OUTPUT: (READ,),
    JUMP_IF_TRUE: (READ, READ),
    JUMP_IF_FALSE: (READ, READ),
    LESS_THAN: (READ, READ, WRITE),
    EQUALS: (READ, READ, WRITE),
    BASE_ADJUST: (READ,),
    HALT: (),
}

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
RIGHT = 1
LEFT = -1
NORTH, EAST, SOUTH, WEST = DIRECTIONS
CARDINALS = (NORTH, SOUTH, WEST, EAST)


class Computer:
    def __init__(
        self, program: str = "", input_: int | list[int] | None = None
    ) -> None:
        self.original_program: dict[int, int] = (
            self.parse(program) if program else defaultdict(int)
        )
        if input_ is None:
            self.input: deque[int | list[int]] = deque()
        elif isinstance(input_, int):
            self.input = deque([input_])
        else:
            self.input = deque(input_)
        self.running = False
        self.pointer: int = 0
        self.output: deque[int] = deque()
        self.program: dict[int, int] = {}
        self.base: int = 0
        self.reset()

    def reset(self) -> None:
        self.program = deepcopy(self.original_program)
        self.pointer = 0
        self.output = deque()
        self.running = True
        self.base = 0

    def overwrite(self) -> None:
        self.original_program = deepcopy(self.program)

    def halt(self) -> None:
        self.running = False

    @staticmethod
    def parse(data: str) -> dict[int, int]:
        return defaultdict(int, {i: int(val) for i, val in enumerate(data.split(","))})

    def __getitem__(self, index: int) -> int:
        return self.program[index]

    def __setitem__(self, index: int, value: int) -> None:
        self.program[index] = value

    def push(self, value: int | list[int]) -> None:
        if isinstance(value, int):
            self.input.append(value)
        else:
            self.input.extend(value)

    def pop(self) -> int:
        return self.output.popleft()

    def pop_many(self, amount: int = 1) -> Generator[int, None, None]:
        return (self.output.popleft() for _ in range(amount))

    @property
    def state(self) -> int:
        return self.program[0]

    def get_args(self, parameter_kinds: tuple[int, ...], modes: int) -> list[int]:
        args: list[int] = [-1] * 3

        for i, kind in enumerate(parameter_kinds):
            a = self[self.pointer + 1 + i]
            mode = modes % 10
            modes //= 10

            if mode == RELATIVE:
                a += self.base
            if mode in (POSITION, RELATIVE):
                if kind == READ:
                    a = self[a]
            elif mode == IMMEDIATE:
                pass

            args[i] = a

        return args

    def run(self) -> None:
        while self.running:
            instruction = self[self.pointer]
            opcode = instruction % 100
            modes = instruction // 100
            parameter_kinds = OPCODES[opcode]
            a, b, c = self.get_args(parameter_kinds, modes)
            self.pointer += 1 + len(parameter_kinds)
            if opcode == ADD:
                self[c] = a + b
            elif opcode == MULT:
                self[c] = a * b
            elif opcode == INPUT:
                if not self.input:
                    self.pointer -= 2
                    break
                new_input = self.input.popleft()
                assert isinstance(new_input, int)
                self[a] = new_input
            elif opcode == OUTPUT:
                self.output.append(a)
            elif opcode == LESS_THAN:
                self[c] = 1 if a < b else 0
            elif opcode == EQUALS:
                self[c] = 1 if a == b else 0
            elif opcode == JUMP_IF_TRUE:
                if a:
                    self.pointer = b or 0
            elif opcode == JUMP_IF_FALSE:
                if not a:
                    self.pointer = b or 0
            elif opcode == BASE_ADJUST:
                self.base += a
            elif opcode == HALT:
                self.pointer -= 1
                self.halt()
            else:
                raise ValueError(f"{opcode} opcode not implemented")


class Robot(Computer):
    def __init__(self, program: str = "", starting_panel: int = 0) -> None:
        super().__init__(program=program)
        self.x, self.y = 0, 0
        self.direction = 0
        self.visited: dict[tuple[int, int], int] = defaultdict(
            int, {(0, 0): starting_panel}
        )

    def move(self) -> None:
        while self.running:
            self.push(self.visited[self.coordinates])
            self.run()
            self.visited[self.coordinates] = self.pop()
            self.rotate(self.pop())
            self.advance()

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.x, self.y

    def advance(self) -> None:
        self.x += DIRECTIONS[self.direction][0]
        self.y += DIRECTIONS[self.direction][1]

    def rotate(self, value: int) -> None:
        self.direction = (self.direction + (RIGHT if value == 1 else LEFT)) % len(
            DIRECTIONS
        )


class Arcade(Computer):
    def __init__(
        self, program: str = "", input_: int | list[int] | None = None
    ) -> None:
        super().__init__(program=program, input_=input_)
        self.score = 0
        self.paddle = (0, 0)
        self.ball = (0, 0)

    def get_tile(self) -> None:
        x, y, t = self.pop_many(3)
        if x == -1 and y == 0:
            self.score = t
        elif t == 3:
            self.paddle = (x, y)
        elif t == 4:
            self.ball = (x, y)

    def autoplay(self) -> None:
        while self.running:
            self.run()
            while self.output:
                self.get_tile()
            self.adjust_paddle()

    def adjust_paddle(self) -> None:
        if self.paddle[0] == self.ball[0]:
            self.push(0)
        elif self.paddle[0] < self.ball[0]:
            self.push(1)
        elif self.paddle[0] > self.ball[0]:
            self.push(-1)


class Droid(Computer):
    def __init__(self, program: str = "") -> None:
        super().__init__(program=program)
        self.x, self.y = 0, 0

    def move(self, direction: int) -> int:
        self.push(direction)
        self.run()
        output = self.pop()
        if output > 0:
            vector = CARDINALS[direction - 1]
            self.x += vector[0]
            self.y += vector[1]
        return output

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.x, self.y
