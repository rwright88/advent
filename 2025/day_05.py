# Day 5


def p1():
    data = []
    with open("2025/input/day-05.txt") as f:
        data = f.read().splitlines()
    split = data.index("")
    ranges = data[:split]
    ingredients = data[split + 1 :]
    count = 0
    for i in ingredients:
        for r in ranges:
            lu = r.split("-")
            l = int(lu[0])
            u = int(lu[1]) + 1
            if int(i) in range(l, u):
                count += 1
                break
    print(count)


if __name__ == "__main__":
    p1()
