# Day 7

import re


def f1():
    data = {}
    cd = ""
    with open("input/day-07.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            if line[:4] == "$ cd":
                if line[5:] == "/":
                    cd = "/"
                elif line[5:] == "..":
                    cd = re.sub("/[^/]*$", "", cd)
                else:
                    cd = f"{cd}/{line[5:]}"
            elif line == "$ ls":
                continue
            elif line[:3] == "dir":
                continue
            else:
                size, file1 = line.split(" ")
                size = int(size)
                if cd not in data:
                    data[cd] = size
                else:
                    data[cd] = data[cd] + size
    for dir1, size in data.copy().items():
        while dir1 != "/":
            parent = re.sub("/[^/]*$", "", dir1)
            if parent not in data:
                data[parent] = size
            else:
                data[parent] = data[parent] + size
            dir1 = parent
    return data


def f2(data):
    unused = 70000000 - data["/"]
    needed = 30000000 - unused
    out = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]) if v >= needed}
    print(min(out.values()))


if __name__ == "__main__":
    data = f1()
    print(sum({k: v for k, v in data.items() if v <= 100000}.values()))
    f2(data)
