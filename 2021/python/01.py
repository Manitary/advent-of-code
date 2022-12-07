with open("input1.txt") as f:
    val = [int(i) for i in f.readlines()]

sums = [val[i] + val[i + 1] + val[i + 2] for i in range(0, len(val) - 2)]


def IncrementCount(x):
    count = 0
    for i in range(0, len(x) - 1):
        if x[i] < x[i + 1]:
            count += 1
    return count


print(IncrementCount(val))
print(IncrementCount(sums))

with open("day1.txt", "w") as o:
    o.write(str(IncrementCount(val)) + "\n")
    o.write(str(IncrementCount(sums)))
