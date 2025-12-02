# Day 2


def p1():
    invalids = []
    with open("2025/input/day-02.txt") as f:
        data = f.read().replace("\n", "")
        data = data.split(",")
        for r in data:
            lower, upper = r.split("-")
            ids = list(range(int(lower), int(upper) + 1))
            for x in ids:
                xs = str(x)
                length = len(xs)
                half = length // 2
                if xs[:half] == xs[half:]:
                    invalids.append(x)
    print(sum(invalids))


def p2():
    invalids = []
    with open("2025/input/day-02.txt") as f:
        data = f.read().replace("\n", "")
        data = data.split(",")
        for r in data:
            lower, upper = r.split("-")
            ids = list(range(int(lower), int(upper) + 1))
            for x in ids:
                xs = str(x)
                length = len(xs)
                half = length // 2
                for i in range(1, half + 1):
                    reps = length // i
                    if xs[:i] * reps == xs:
                        invalids.append(x)
                        break
    print(sum(invalids))


if __name__ == "__main__":
    p1()
    p2()
