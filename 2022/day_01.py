# Day 1

data = []
total = []
with open("input/day-01.txt") as f:
    for line in f:
        cals = line.replace("\n", "")
        if cals != "":
            total.append(int(cals))
        else:
            data.append(sum(total))
            total = []
print(max(data))
print(sum(sorted(data, reverse=True)[:3]))
