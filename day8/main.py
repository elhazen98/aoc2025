from collections import defaultdict

with open("data.txt", encoding="utf-8") as f:
    origin = [line.strip() for line in f]

origin = [[int(n) for n in num.split(",")] for num in origin]

test = [[162, 817, 812],
        [57, 618, 57],
        [906, 360, 560],
        [592, 479, 940],
        [352, 342, 300],
        [466, 668, 158],
        [542, 29, 236],
        [431, 825, 988],
        [739, 650, 466],
        [52, 470, 668],
        [216, 146, 977],
        [819, 987, 18],
        [117, 168, 530],
        [805, 96, 715],
        [346, 949, 466],
        [970, 615, 88],
        [941, 993, 340],
        [862, 61, 35],
        [984, 92, 344],
        [425, 690, 689]]


def count(data, times):
    N = len(data)
    ls = []
    for i in range(N):
        x1, y1, z1 = data[i]
        for j in range(i + 1, N):
            x2, y2, z2 = data[j]
            dist = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            ls.append((dist, i, j))

    ls.sort()

    nodes = defaultdict(list)
    for t in range(times):
        _, i, j = ls[t]
        nodes[i].append(j)
        nodes[j].append(i)

    def dfs(node):
        if node in visited:
            return 0
        n_nodes = 1
        visited.add(node)
        for next_node in nodes[node]:
            n_nodes += dfs(next_node)

        return n_nodes

    visited = set()
    groups = []
    for node, _ in nodes.items():
        if node not in visited:
            groups.append(dfs(node))

    groups.sort(reverse=True)
    res = 1
    for i in range(3):
        res *= groups[i]

    return res


def count2(n, ls, times):

    nodes = defaultdict(list)
    for t in range(times):
        _, i, j = ls[t]
        nodes[i].append(j)
        nodes[j].append(i)

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for next_node in nodes[node]:
            dfs(next_node)

    visited = set()
    if 0 not in nodes:
        return False
    else:
        dfs(0)
        return len(visited) == n


def bs(data):

    N = len(data)
    ls = []
    for i in range(N):
        x1, y1, z1 = data[i]
        for j in range(i + 1, N):
            x2, y2, z2 = data[j]
            dist = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            ls.append((dist, i, j))

    ls.sort()
    l = 1
    r = len(ls)
    while l < r:
        m = (l + r) // 2
        isConnect = count2(N, ls, m)
        if isConnect:
            r = m
        else:
            l = m + 1

    _, i, j = ls[l - 1]
    return data[i][0] * data[j][0]


print(count(origin, 1000))
print(bs(origin))
