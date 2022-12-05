# Day 5


def f1():
    data = []
    with open("input/day-05.txt") as f:
        for line in f:
            data.append(line.replace("\n", ""))
    ind = data.index("")
    stacks = data[:ind]
    positions = stacks[-1]
    n_stacks = max([int(x) for x in positions.split(" ") if x != ""])
    positions = [i for i, pos in enumerate(positions) if pos != " "]
    stacks.reverse()
    cols = [[] for _ in range(n_stacks)]
    for row in stacks[1:]:
        length = len(row)
        for i, p in enumerate(positions):
            if p < length:
                crate = row[p]
                if crate != " ":
                    cols[i].append(crate)
    proc = data[(ind + 1):]
    for p in proc:
        p = p[5:].split(" from ")
        move = int(p[0])
        start, end = p[1].split(" to ")
        start = int(start) - 1
        end = int(end) - 1
        for _ in range(move):
            crate = cols[start].pop()
            cols[end].append(crate)
    print("".join([col[-1] for col in cols]))


def f2():
    data = []
    with open("input/day-05.txt") as f:
        for line in f:
            data.append(line.replace("\n", ""))
    ind = data.index("")
    stacks = data[:ind]
    positions = stacks[-1]
    n_stacks = max([int(x) for x in positions.split(" ") if x != ""])
    positions = [i for i, pos in enumerate(positions) if pos != " "]
    stacks.reverse()
    cols = [[] for _ in range(n_stacks)]
    for row in stacks[1:]:
        length = len(row)
        for i, p in enumerate(positions):
            if p < length:
                crate = row[p]
                if crate != " ":
                    cols[i].append(crate)
    proc = data[(ind + 1):]
    for p in proc:
        p = p[5:].split(" from ")
        move = int(p[0])
        start, end = p[1].split(" to ")
        start = int(start) - 1
        end = int(end) - 1
        crates = cols[start][-move:]
        del cols[start][-move:]
        cols[end].extend(crates)
    print("".join([col[-1] for col in cols]))


if __name__ == "__main__":
    f1()
    f2()
