# Day 9


def f1():
    T = []
    h = [0, 0]
    t = [0, 0]
    with open("input/day-09.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            direction, size = line.split(" ")
            size = int(size)
            if direction == "L":
                for _ in range(size):
                    h[0] = h[0] - 1
                    if (h[0] - t[0] == -2) and (h[1] != t[1]):
                        t[0] = t[0] - 1
                        t[1] = h[1]
                    elif h[0] - t[0] == -2:
                        t[0] = t[0] - 1
                    T.append(t.copy())
            elif direction == "R":
                for _ in range(size):
                    h[0] = h[0] + 1
                    if (h[0] - t[0] == 2) and (h[1] != t[1]):
                        t[0] = t[0] + 1
                        t[1] = h[1]
                    elif h[0] - t[0] == 2:
                        t[0] = t[0] + 1
                    T.append(t.copy())
            elif direction == "U":
                for _ in range(size):
                    h[1] = h[1] + 1
                    if (h[1] - t[1] == 2) and (h[0] != t[0]):
                        t[1] = t[1] + 1
                        t[0] = h[0]
                    elif h[1] - t[1] == 2:
                        t[1] = t[1] + 1
                    T.append(t.copy())
            elif direction == "D":
                for _ in range(size):
                    h[1] = h[1] - 1
                    if (h[1] - t[1] == -2) and (h[0] != t[0]):
                        t[1] = t[1] - 1
                        t[0] = h[0]
                    elif h[1] - t[1] == -2:
                        t[1] = t[1] - 1
                    T.append(t.copy())
    print(len([list(x) for x in set(tuple(x) for x in T)]))


def f2():
    T = []
    rope = [[0, 0] for _ in range(10)]
    with open("input/day-09.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            direction, size = line.split(" ")
            size = int(size)
            if direction == "L":
                for _ in range(size):
                    rope[0][0] = rope[0][0] - 1
                    for i in range(9):
                        j = i + 1
                        x_diff = rope[i][0] - rope[j][0]
                        y_diff = rope[i][1] - rope[j][1]
                        step = move(x_diff, y_diff)
                        rope[j][0] = rope[j][0] + step[0]
                        rope[j][1] = rope[j][1] + step[1]
                    T.append(rope[9].copy())
            elif direction == "R":
                for _ in range(size):
                    rope[0][0] = rope[0][0] + 1
                    for i in range(9):
                        j = i + 1
                        x_diff = rope[i][0] - rope[j][0]
                        y_diff = rope[i][1] - rope[j][1]
                        step = move(x_diff, y_diff)
                        rope[j][0] = rope[j][0] + step[0]
                        rope[j][1] = rope[j][1] + step[1]
                    T.append(rope[9].copy())
            elif direction == "U":
                for _ in range(size):
                    rope[0][1] = rope[0][1] + 1
                    for i in range(9):
                        j = i + 1
                        x_diff = rope[i][0] - rope[j][0]
                        y_diff = rope[i][1] - rope[j][1]
                        step = move(x_diff, y_diff)
                        rope[j][0] = rope[j][0] + step[0]
                        rope[j][1] = rope[j][1] + step[1]
                    T.append(rope[9].copy())
            elif direction == "D":
                for _ in range(size):
                    rope[0][1] = rope[0][1] - 1
                    for i in range(9):
                        j = i + 1
                        x_diff = rope[i][0] - rope[j][0]
                        y_diff = rope[i][1] - rope[j][1]
                        step = move(x_diff, y_diff)
                        rope[j][0] = rope[j][0] + step[0]
                        rope[j][1] = rope[j][1] + step[1]
                    T.append(rope[9].copy())
    print(len([list(x) for x in set(tuple(x) for x in T)]))


def move(x_diff, y_diff):
    if x_diff == 0 and y_diff == 2:
        step = [0, 1]
    elif x_diff == 2 and y_diff == 0:
        step = [1, 0]
    elif x_diff == 0 and y_diff == -2:
        step = [0, -1]
    elif x_diff == -2 and y_diff == 0:
        step = [-1, 0]
    elif (
        (x_diff == 1 and y_diff == 2)
        or (x_diff == 2 and y_diff == 2)
        or (x_diff == 2 and y_diff == 1)
    ):
        step = [1, 1]
    elif (
        (x_diff == 2 and y_diff == -1)
        or (x_diff == 2 and y_diff == -2)
        or (x_diff == 1 and y_diff == -2)
    ):
        step = [1, -1]
    elif (
        (x_diff == -1 and y_diff == -2)
        or (x_diff == -2 and y_diff == -2)
        or (x_diff == -2 and y_diff == -1)
    ):
        step = [-1, -1]
    elif (
        (x_diff == -2 and y_diff == 1)
        or (x_diff == -2 and y_diff == 2)
        or (x_diff == -1 and y_diff == 2)
    ):
        step = [-1, 1]
    else:
        step = [0, 0]
    return step


if __name__ == "__main__":
    f1()
    f2()
