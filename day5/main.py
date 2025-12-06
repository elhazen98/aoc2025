with open("data.txt", encoding="utf-8") as f:
    origin = [line.strip() for line in f]

test = ["3-5", "10-14", "16-20", "12-18", "", "1", "5", "8", "11", "17", "32"]


def count(data):
    ingredients = []
    i = 0
    while data[i] != "":
        a, b = data[i].split("-")
        ingredients.append([int(a), -1])
        ingredients.append([int(b), 1])
        i += 1

    i += 1
    while i < len(data):
        ingredients.append([int(data[i]), 0])
        i += 1

    ingredients.sort()
    res = 0
    cur = 0
    for _, s in ingredients:
        cur += s
        if s == 0 and cur < 0:
            res += 1

    return res


def fresh_only(data):
    ingredients = []
    i = 0
    while data[i] != "":
        a, b = data[i].split("-")
        ingredients.append([int(a), -1])
        ingredients.append([int(b), 1])
        i += 1

    ingredients.sort()
    res = 0
    cur = 0
    start = 0
    for id, s in ingredients:
        if cur == 0:
            start = id
        cur += s
        if cur == 0:
            res += id - start + 1

    return res


print(fresh_only(origin))
