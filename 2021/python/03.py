with open("input3.txt") as f:
    report = f.read().splitlines()

l = len(report[0])
mask = 2**l - 1

gamma = ""
for i in range(0, l):
    gamma += "1" if [num[i] for num in report].count("1") > len(report) / 2 else "0"

gamma = int(gamma, 2)
power = gamma * (~gamma & mask)


def FilterList(a, i, b):
    if len(a) == 1:
        return a
    val = b if [num[i] for num in a].count("1") >= len(a) / 2 else (1 - b)
    return list(filter(lambda x: x[i] == str(val), a))


oxygen = report
co2 = report
for i in range(0, l):
    oxygen = FilterList(oxygen, i, 1)
    co2 = FilterList(co2, i, 0)

lifesupport = int(oxygen[0], 2) * int(co2[0], 2)

with open("day3.txt", "w") as o:
    o.write(str(power))
    o.write("\n")
    o.write(str(lifesupport))
