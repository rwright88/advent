# Day 8

import math


def f1():
    data = []
    with open("input/day-08.txt") as f:
        for line in f:
            line = [int(x) for x in list(line.replace("\n", ""))]
            data.append(line)
    n = 0
    nrows = len(data)
    ncols = len(data[0])
    for row in range(nrows):
        for col in range(ncols):
            if (row == 0) or (col == 0) or (row == nrows - 1) or (col == ncols - 1):
                n = n + 1
            else:
                val = data[row][col]
                val_row = data[row]
                val_col = [r[col] for r in data]
                if (
                    (val > max(val_row[:col]))
                    or (val > max(val_row[(col + 1) :]))
                    or (val > max(val_col[:row]))
                    or (val > max(val_col[(row + 1) :]))
                ):
                    n = n + 1
    print(n)


def f2():
    data = []
    with open("input/day-08.txt") as f:
        for line in f:
            line = [int(x) for x in list(line.replace("\n", ""))]
            data.append(line)
    scores = []
    nrows = len(data)
    ncols = len(data[0])
    for row in range(nrows):
        for col in range(ncols):
            val = data[row][col]
            val_row = data[row]
            val_col = [r[col] for r in data]
            l = val_row[:col]
            l.reverse()
            r = val_row[(col + 1) :]
            u = val_col[:row]
            u.reverse()
            d = val_col[(row + 1) :]
            score = []
            for vector in [l, r, u, d]:
                score_vec = 0
                if len(vector) == 0:
                    score.append(score_vec)
                    continue
                for i, v in enumerate(vector):
                    score_vec = score_vec + 1
                    if (v >= val) or (i == len(vector) - 1):
                        score.append(score_vec)
                        break
            score = math.prod(score)
            scores.append(score)
    print(max(scores))


if __name__ == "__main__":
    f1()
    f2()
