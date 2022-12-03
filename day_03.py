# Day 3

import string

chars = string.ascii_lowercase + string.ascii_uppercase

total = 0
with open("input/day-03.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        length = len(line)
        half = int(length / 2)
        part1 = line[:half]
        part2 = line[half:]
        same = list(set(part1) & set(part2))[0]
        total = total + (chars.find(same) + 1)
print(total)

total = 0
r_num = 0
badge = ""
with open("input/day-03.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        if r_num == 0:
            badge = line
        elif r_num == 1:
            badge = list(set(badge) & set(line))
        elif r_num == 2:
            badge = list(set(badge) & set(line))[0]
            score = chars.find(badge) + 1
            total = total + score
            badge = ""
        r_num = r_num + 1
        if r_num == 3:
            r_num = 0
print(total)
