with open("data.txt", encoding="utf-8") as f:
    origin = [line.strip() for line in f]

origin = [row for i, row in enumerate(origin) if i % 2 == 0]

test = [".......S.......",
        ".......^.......",
        "......^.^......",
        ".....^.^.^.....",
        "....^.^...^....",
        "...^.^...^.^...",
        "..^...^.....^..",
        ".^.^.^.^.^...^."]


def count(data):
    ROW = len(data)
    COL = len(data[0])
    seen = set()

    path = []
    for i, s in enumerate(data[0]):
        if s == 'S':
            path.append([0, i])
            seen.add((0, i))

    res = 0
    while len(path) > 0:
        r, c = path.pop()
        if r + 1 < ROW:
            if data[r + 1][c] == "^":
                res += 1
                if c + 1 < COL and (r + 1, c + 1) not in seen:
                    path.append([r + 1, c + 1])
                    seen.add((r + 1, c + 1))
                if c - 1 >= 0 and (r + 1, c - 1) not in seen:
                    path.append([r + 1, c - 1])
                    seen.add((r + 1, c - 1))
            else:
                if (r + 1, c) not in seen:
                    path.append([r + 1, c])
                    seen.add((r + 1, c))
    return res


def count2(data):
    ROW = len(data)
    COL = len(data[0])
    seen = {}

    def dfs(r, c):
        if c < 0 or c >= COL:
            return 0
        if r >= ROW:
            return 1
        if (r, c) in seen:
            return seen[(r, c)]

        cur = 0
        if data[r][c] == "^":
            cur += dfs(r + 1, c - 1) + dfs(r + 1, c + 1)
        else:
            cur += dfs(r + 1, c)

        seen[(r, c)] = cur
        return cur

    res = 0
    for i, s in enumerate(data[0]):
        if s == 'S':
            res += dfs(1, i)
            break

    return res


print(count2(test))
print(count2(origin))
