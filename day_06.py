# Day 6


def f1():
    with open("input/day-06.txt") as f:
        data = f.readline().replace("\n", "")
    for i in range(len(data)):
        if i < 3:
            continue
        chars = data[(i - 3):(i + 1)]
        if len(set(chars)) == 4:
            print(i + 1)
            break


def f2():
    with open("input/day-06.txt") as f:
        data = f.readline().replace("\n", "")
    for i in range(len(data)):
        if i < 13:
            continue
        chars = data[(i - 13):(i + 1)]
        if len(set(chars)) == 14:
            print(i + 1)
            break


if __name__ == "__main__":
    f1()
    f2()
