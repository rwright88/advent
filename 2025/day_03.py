# Day 3


def p1():
    data = []
    with open("2025/input/day-03.txt") as f:
        for line in f:
            bank = list(line.strip())
            j1 = max(bank)
            if bank.index(j1) == len(bank) - 1:
                j1 = max(bank[:-1])
            i1 = bank.index(j1)
            j2 = max(bank[(i1 + 1) :])
            data.append(int(f"{j1}{j2}"))
    print(sum(data))


def p2():
    data = []
    with open("2025/input/day-03.txt") as f:
        for line in f:
            bank = list(line.strip())
            length = len(bank)
            j = []
            inds = []
            for i in range(12):
                if i == 0:
                    end = length - 12 + 1
                    e = max(bank[:end])
                    ind = bank.index(e)
                else:
                    start = inds[-1] + 1
                    end = length - (12 - i) + 1
                    e = max(bank[start:end])
                    ind = bank.index(e, start, end)
                j.append(e)
                inds.append(ind)
            data.append(int("".join(j)))
    print(sum(data))


if __name__ == "__main__":
    p1()
    p2()
