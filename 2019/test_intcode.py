from intcode import Computer
from collections import deque
from aocd import get_data

def test_creation():
    bot = Computer()
    assert isinstance(bot, Computer)
    assert not bot.program
    assert not bot.input
    assert not bot.output
    assert bot.pointer == 0

def test_input_parsing():
    data = "1,9,10,3,2,3,11,0,99,30,40,50"
    bot = Computer(data)
    assert all(int(num) == bot[i] for i, num in enumerate(data.split(',')))
    assert bot.state == 1

def test_alteration():
    data = "1,2,3"
    bot = Computer(data)
    bot[1] = 10
    assert bot[0] == 1
    assert bot[1] == 10
    assert bot[2] == 3

def test_day2_1():
    data = "1,9,10,3,2,3,11,0,99,30,40,50"
    bot = Computer(data)
    bot.run()
    assert bot.state == 3500
    assert bot[3] == 70
    assert all(int(num) == bot[i] for i, num in enumerate(data.split(',')) if i != 0 and i != 3)

def test_day2_sum():
    data = "1,0,0,0,99"
    bot = Computer(data)
    bot.run()
    assert bot.state == 2
    assert all(int(num) == bot[i] for i, num in enumerate(data.split(',')) if i != 0)

def test_day2_prod_1():
    data = "2,3,0,3,99"
    bot = Computer(data)
    bot.run()
    assert bot[3] == 6
    assert all(int(num) == bot[i] for i, num in enumerate(data.split(',')) if i != 3)

def test_day2_prod_2():
    data = "2,4,4,5,99,0"
    bot = Computer(data)
    bot.run()
    assert bot[5] == 9801
    assert all(int(num) == bot[i] for i, num in enumerate(data.split(',')) if i != 5)

def test_day2_sum_prod():
    data = "1,1,1,4,99,5,6,0,99"
    bot = Computer(data)
    bot.run()
    assert bot.state == 30
    assert bot[4] == 2
    assert all(int(num) == bot[i] for i, num in enumerate(data.split(',')) if i != 0 and i != 4)

def test_day2_part1():
    data = get_data(day=2, year=2019)
    bot = Computer(data)
    bot[1] = 12
    bot[2] = 2
    bot.run()
    assert bot.state == 6568671

def test_day2_part2():
    data = get_data(day=2, year=2019)
    bot = Computer(data)
    bot[1] = 39
    bot[2] = 51
    bot.run()
    assert bot.state == 19690720

def test_day5_IO_1():
    data = "3,0,4,0,99"
    bot = Computer(data)
    bot.push(1)
    bot.run()
    assert bot.pop() == 1
    assert not bot.output

def test_day5_IO_2():
    data = "3,0,4,0,99"
    bot = Computer(data, [1, 2, 3])
    bot.run()
    assert list(bot.input) == [2, 3]
    assert bot.pop() == 1
    assert not bot.output

def test_day5_immediate_mode_1():
    data = "1002,4,3,4,33"
    bot = Computer(data)
    bot.run()
    assert bot[4] == 99
    assert all(int(num) == bot[i] for i, num in enumerate(data.split(',')) if i != 4)

def test_day5_immediate_mode_2():
    data = "1101,100,-1,4,0"
    bot = Computer(data)
    bot.run()
    assert bot[4] == 99

def test_day5_equals_1():
    data = "3,9,8,9,10,9,4,9,99,-1,8"
    inputs = list(range(-5, 15))
    outputs = []
    for i in inputs:
        bot = Computer(data)
        bot.push(i)
        bot.run()
        outputs.append(bot.pop())

    for i, value in enumerate(inputs):
        assert bool(outputs[i]) == bool(value == 8)

def test_day5_equals_2():
    data = "3,3,1108,-1,8,3,4,3,99"
    inputs = list(range(-5, 15))
    outputs = []
    for i in inputs:
        bot = Computer(data)
        bot.push(i)
        bot.run()
        outputs.append(bot.pop())

    for i, value in enumerate(inputs):
        assert bool(outputs[i]) == bool(value == 8)

def test_day5_equals_3():
    data = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    inputs = list(range(-5, 15))
    outputs = []
    for i in inputs:
        bot = Computer(data)
        bot.push(i)
        bot.run()
        outputs.append(bot.pop())

    for i, value in enumerate(inputs):
        assert bool(outputs[i]) == bool(value != 0)

def test_day5_equals_4():
    data = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    inputs = list(range(-5, 15))
    outputs = []
    for i in inputs:
        bot = Computer(data)
        bot.push(i)
        bot.run()
        outputs.append(bot.pop())

    for i, value in enumerate(inputs):
        assert bool(outputs[i]) == bool(value != 0)

def test_day5_lessthan_1():
    data = "3,9,7,9,10,9,4,9,99,-1,8"
    inputs = list(range(-5, 15))
    outputs = []
    for i in inputs:
        bot = Computer(data)
        bot.push(i)
        bot.run()
        outputs.append(bot.pop())

    for i, value in enumerate(inputs):
        assert bool(outputs[i]) == bool(value < 8)

def test_day5_lessthan_2():
    data = "3,3,1107,-1,8,3,4,3,99"
    inputs = list(range(-5, 15))
    outputs = []
    for i in inputs:
        bot = Computer(data)
        bot.push(i)
        bot.run()
        outputs.append(bot.pop())

    for i, value in enumerate(inputs):
        assert bool(outputs[i]) == bool(value < 8)

def test_day5_comparison():
    data = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    inputs = list(range(-5, 15))
    outputs = []
    for i in inputs:
        bot = Computer(data)
        bot.push(i)
        bot.run()
        outputs.append(bot.pop())

    for i, value in enumerate(inputs):
        if value < 8:
            assert outputs[i] == 999
        elif value == 8:
            assert outputs[i] == 1000
        elif value > 8:
            assert outputs[i] == 1001

def test_day5_part1():
    data = get_data(day=5, year=2019)
    bot = Computer(data, [1])
    bot.run()
    while len(bot.output) > 1:
        assert bot.pop() == 0
    assert bot.pop() == 7988899
    assert not bot.output

def test_day5_part2():
    data = get_data(day=5, year=2019)
    bot = Computer(data)
    bot.push(5)
    bot.run()
    while len(bot.output) > 1:
        assert bot.pop() == 0
    assert bot.pop() == 13758663
    assert not bot.output
