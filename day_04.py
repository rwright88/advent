# Day 3

total = 0
with open("input/day-04.txt") as f:
    for line in f:
        line = line.strip()
        elf1, elf2 = line.split(",")
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        range1 = list(range(int(elf1[0]), int(elf1[1]) + 1))
        range2 = list(range(int(elf2[0]), int(elf2[1]) + 1))
        fully = all([r1 in range2 for r1 in range1]) or all([r2 in range1 for r2 in range2])
        if fully:
            total = total + 1
print(total)

total = 0
with open("input/day-04.txt") as f:
    for line in f:
        line = line.strip()
        elf1, elf2 = line.split(",")
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        range1 = list(range(int(elf1[0]), int(elf1[1]) + 1))
        range2 = list(range(int(elf2[0]), int(elf2[1]) + 1))
        fully = any([r1 in range2 for r1 in range1]) or any([r2 in range1 for r2 in range2])
        if fully:
            total = total + 1
print(total)
