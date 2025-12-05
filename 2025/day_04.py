# Day 4


def p1():
    data = []
    count = 0
    with open("2025/input/day-04.txt") as f:
        for line in f:
            data.append(list(line.strip()))
    for i in range(len(data)):
        for j in range(len(data[i])):
            if sum_surrounding(data, i, j) < 4 and data[i][j] == "@":
                count += 1
    print(count)


def p2():
    data = []
    with open("2025/input/day-04.txt") as f:
        for line in f:
            data.append(list(line.strip()))
    count = 0
    count_run = 1
    while count_run > 0:
        count_run = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if sum_surrounding(data, i, j) < 4 and data[i][j] == "@":
                    count += 1
                    count_run += 1
                    data[i][j] = "."
    print(count)


def sum_surrounding(data, i, j):
    return (
        surround(data, i - 1, j - 1)
        + surround(data, i - 1, j)
        + surround(data, i - 1, j + 1)
        + surround(data, i, j - 1)
        + surround(data, i, j + 1)
        + surround(data, i + 1, j - 1)
        + surround(data, i + 1, j)
        + surround(data, i + 1, j + 1)
    )


def surround(data, i, j):
    if i >= 0 and j >= 0 and i < len(data) and j < len(data[i]):
        return data[i][j] == "@"
    else:
        return 0


if __name__ == "__main__":
    p1()
    p2()
