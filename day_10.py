# Day 10


def f1():
    cycles = []
    with open("input/day-10.txt") as f:
        for line in f:
            cycles.append(line.replace("\n", ""))
    n = 1
    x = 1
    adds = []
    res = [1]
    for cycle in cycles:
        if cycle == "noop":
            adds.append(0)
        if cycle != "noop":
            command, value = cycle.split(" ")
            value = int(value)
            adds.extend([0, value])
        x = x + adds[0]
        adds = adds[1:]
        n = n + 1
        res.append(x * n)
    for _ in range(len(adds)):
        x = x + adds[0]
        adds = adds[1:]
        n = n + 1
        res.append(x * n)
    print(res[19] + res[59] + res[99] + res[139] + res[179] + res[219])


def f2():
    cycles = []
    with open("input/day-10.txt") as f:
        for line in f:
            cycles.append(line.replace("\n", ""))
    n = 1
    x = 1
    adds = []
    res = ["#"]
    for cycle in cycles:
        if cycle == "noop":
            adds.append(0)
        if cycle != "noop":
            command, value = cycle.split(" ")
            value = int(value)
            adds.extend([0, value])
        x = x + adds[0]
        adds = adds[1:]
        n = n + 1
        if abs((n - 1) % 40 - x) <= 1:
            res.append("#")
        else:
            res.append(" ")
    for _ in range(len(adds)):
        x = x + adds[0]
        adds = adds[1:]
        n = n + 1
        if abs((n - 1) % 40 - x) <= 1:
            res.append("#")
        else:
            res.append(" ")
    res = "".join(res)
    for i in range(0, 241, 40):
        print(res[i:(i + 40)])


if __name__ == "__main__":
    f1()
    f2()
