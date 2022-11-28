from typing import Union

class Computer:
    def __init__(self, program: str = None, input_: Union[int, list[int]] = None):
        self.setProgram(program, input_)

    @staticmethod
    def parse(data: str):
        return {i: int(val) for i, val in enumerate(data.split(','))}

    def run(self):
        while True:
            opcode = self.valuePointer(self.pointer) % 100
            match opcode:
                case 99:
                    break
                case 1:
                    self.add(self.pointer)
                    yield None
                case 2:
                    self.mult(self.pointer)
                    yield None
                case 3:
                    self.readInput(self.pointer)
                    yield None
                case 4:
                    self.setOutput(self.pointer)
                    yield self.getOutput
                case 5:
                    self.jumpIfTrue(self.pointer)
                    yield None
                case 6:
                    self.jumpIfFalse(self.pointer)
                    yield None
                case 7:
                    self.lessThan(self.pointer)
                    yield None
                case 8:
                    self.equal(self.pointer)
                    yield None
                case _:
                    raise ValueError("Unknown opcode")
    
    def setProgram(self, program: str = None, input_: Union[int, list[int]] = None):
        if program:
            self.program = self.parse(program)
            if input_:
                self.setInput(input_)
        else:
            self.program = {}
        self.pointer = 0
    
    def getValue(self, position: int, parameter_index: int):
        number = (self.valuePointer(self.pointer) // (10 * 10**parameter_index)) % 10
        match number:
            case 0:
                return self.valueTarget(position + parameter_index)
            case 1:
                return self.valuePointer(position + parameter_index)
        raise ValueError('Unknown mode')

    @property
    def state(self):
        return self.program[0]

    def replace(self, position: int, value: int):
        self.program[position] = value
    
    def valuePointer(self, position: int):
        return self.program[position]
    
    def valueTarget(self, position: int):
        return self.program[self.valuePointer(position)]

    def add(self, position: int):
        self.program[self.valuePointer(position + 3)] = self.getValue(position, 1) + self.getValue(position, 2)
        self.pointer += 4
    
    def mult(self, position: int):
        self.program[self.valuePointer(position + 3)] = self.getValue(position, 1) * self.getValue(position, 2)
        self.pointer += 4
    
    def setInput(self, value: Union[int, list[int]]):
        if isinstance(value, int):
            self.input = [value]
        elif isinstance(value, list):
            self.input = value
    
    def getInput(self):
        return self.input.pop(0)
    
    @property
    def getOutput(self):
        return self.output
    
    def readInput(self, position: int):
        self.program[self.valuePointer(position + 1)] = self.getInput()
        self.pointer += 2

    def setOutput(self, position: int):
        self.output = self.getValue(position, 1)
        self.pointer += 2
    
    def jumpIfTrue(self, position: int):
        if self.getValue(position, 1) == 0:
            self.pointer += 3
        else:
            self.pointer = self.getValue(position, 2)
    
    def jumpIfFalse(self, position: int):
        if self.getValue(position, 1) == 0:
            self.pointer = self.getValue(position, 2)
        else:
            self.pointer += 3

    def lessThan(self, position: int):
        self.program[self.valuePointer(position + 3)] = 1 if self.getValue(position, 1) < self.getValue(position, 2) else 0
        self.pointer += 4
    
    def equal(self, position: int):
        self.program[self.valuePointer(position + 3)] = 1 if self.getValue(position, 1) == self.getValue(position, 2) else 0
        self.pointer += 4