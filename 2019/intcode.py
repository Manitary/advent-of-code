from typing import Union
from collections import deque

# Modes
POSITION = 0
IMMEDIATE = 1

# Opcodes
ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
HALT = 99

# Role of the parameters for each opcode
READ = 0
WRITE = 1
OPCODES = {
    ADD: (READ, READ, WRITE),
    MULT: (READ, READ, WRITE),
    INPUT: (WRITE,),
    OUTPUT: (READ,),
    JUMP_IF_TRUE: (READ, READ),
    JUMP_IF_FALSE: (READ, READ),
    LESS_THAN: (READ, READ, WRITE),
    EQUALS: (READ, READ, WRITE),
    HALT: (),
}

class Computer:
    def __init__(self, program: str = None, input_: list[int] = None):
        self.setProgram(program, input_)

    def setProgram(self, program: str = None, input_: list[int] = None):
        self.program = self.parse(program) if program else {}
        self.input = deque(input_ or [])
        self.output = deque()
        self.pointer = 0

    @staticmethod
    def parse(data: str):
        return {i: int(val) for i, val in enumerate(data.split(','))}
    
    def __getitem__(self, index):
        return self.program[index]
    
    def __setitem__(self, index, value):
        self.program[index] = value

    def push(self, value):
        self.input.append(value)
    
    def pop(self):
        return self.output.popleft()
    
    @property
    def state(self):
        return self.program[0]
    
    def get_args(self, parameter_kinds: tuple[int], modes: int):
        args = [None] * 3

        for i, kind in enumerate(parameter_kinds):
            a = self[self.pointer + 1 + i]
            mode = modes % 10
            modes //= 10

            if mode == POSITION:
                if kind == READ:
                    a = self[a]
            elif mode == IMMEDIATE:
                pass

            args[i] = a

        return args
    
    def run(self):
        while (instruction := self[self.pointer]) != HALT:
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
                while not self.input:
                    #yield
                    break
                self[a] = self.input.popleft()
            elif opcode == OUTPUT:
                self.output.append(a)
            elif opcode == LESS_THAN:
                self[c] = 1 if a < b else 0
            elif opcode == EQUALS:
                self[c] = 1 if a == b else 0
            elif opcode == JUMP_IF_TRUE:
                if a:
                    self.pointer = b
            elif opcode == JUMP_IF_FALSE:
                if not a:
                    self.pointer = b
            else:
                raise Exception(f"{opcode} opcode not implemented")