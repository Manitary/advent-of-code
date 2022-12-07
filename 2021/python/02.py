with open("input2.txt") as f:
    instr = [l.split() for l in f.readlines()]

x = y = a = 0

for i in instr:
    match i[0][0]:
        case "f":
            x += int(i[1])
            y += int(i[1]) * a
        case "d":
            a += int(i[1])
        case "u":
            a -= int(i[1])

with open("day2.txt", "w") as o:
    o.write(str(x * a))
    o.write("\n")
    o.write(str(x * y))
