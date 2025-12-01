# Day 1


def p1():
    count = 0
    point = 50
    with open("2025/input/day-01.txt") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            amount = int(line[1:])
            if direction == "L":
                point -= amount
            else:
                point += amount
            if point >= 100:
                point = point % 100
            elif point < -99:
                point = point % -100
            if point == 0:
                count += 1
    print(count)


def p2():
    count = 0
    points = [50]
    with open("2025/input/day-01.txt") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            amount = int(line[1:])
            last = points[-1]
            if direction == "L":
                this = last - amount
            else:
                this = last + amount
            if this >= 100:
                count += this // 100
                this = this % 100
                if last < 0 and this == 0:
                    count += 1
            elif this == 0:
                count += 1
            elif this < -99:
                count += this // -100
                this = this % -100
                if last > 0 and this == 0:
                    count += 1
            if last * this < 0:
                count += 1
            points.append(this)
    print(count)


if __name__ == "__main__":
    p1()
    p2()
