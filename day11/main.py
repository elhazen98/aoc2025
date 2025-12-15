from collections import deque

with open("data.txt", encoding="utf-8") as f:
    origin = [line.strip() for line in f]

test = ["aaa: you hhh",
        "you: bbb ccc",
        "bbb: ddd eee",
        "ccc: ddd eee fff",
        "ddd: ggg",
        "eee: out",
        "fff: out",
        "ggg: out",
        "hhh: ccc fff iii",
        "iii: out"]

test2 = ["svr: aaa bbb",
         "aaa: fft",
         "fft: ccc",
         "bbb: tty",
         "tty: ccc",
         "ccc: ddd eee",
         "ddd: hub",
         "hub: fff",
         "eee: dac",
         "dac: fff",
         "fff: ggg hhh",
         "ggg: out",
         "hhh: out"]


def map(data):
    splited = [row.split(":") for row in data]
    maped = {row[0]: row[1][1:].split(" ") for row in splited}
    return maped


def count(data):
    graph = map(data)

    def dfs(pos, dac, fft):
        if pos == "out":
            return 1 if dac and fft else 0
        if (pos, dac, fft) in visited:
            return visited[(pos, dac, fft)]

        if pos == "dac":
            dac = True
        if pos == "fft":
            fft = True

        visited[(pos, dac, fft)] = 0
        next_pos = graph[pos]
        for np in next_pos:
            visited[(pos, dac, fft)] += dfs(np, dac, fft)

        return visited[(pos, dac, fft)]

    visited = {}
    res = dfs("svr", False, False)
    return res


print(count(origin))
