# Day 2

total = 0
with open("input/day-02.txt") as f:
    for line in f:
        score = 0
        them, me = line.replace("\n", "").split(" ")
        if (them == "A" and me == "Y") or (them == "B" and me == "Z") or (them == "C" and me == "X"):
            score = score + 6
        elif (them == "A" and me == "X") or (them == "B" and me == "Y") or (them == "C" and me == "Z"):
            score = score + 3
        if me == "X":
            score = score + 1
        elif me == "Y":
            score = score + 2
        elif me == "Z":
            score = score + 3
        total = total + score
print(total)

total = 0
with open("input/day-02.txt") as f:
    for line in f:
        score = 0
        them, res = line.replace("\n", "").split(" ")
        if res == "Z":
            score = score + 6
        elif res == "Y":
            score = score + 3
        if (res == "X" and them == "B") or (res == "Y" and them == "A") or (res == "Z" and them == "C"):
            score = score + 1
        elif (res == "X" and them == "C") or (res == "Y" and them == "B") or (res == "Z" and them == "A"):
            score = score + 2
        elif (res == "X" and them == "A") or (res == "Y" and them == "C") or (res == "Z" and them == "B"):
            score = score + 3
        total = total + score
print(total)
