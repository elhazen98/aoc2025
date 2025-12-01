with open("data.txt", encoding="utf-8") as f:
    rows = [line.strip() for line in f]

test = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

def count(rows):

    position = 50
    res = 0
    for item in rows:

        dir = item[0]
        num = int(item[1:])
        res += num // 100
        num %= 100

        if dir == "L":
            if position == 0:
                position = 100 - num
                continue
            cur = position - num
            if cur < 0:
                res += 1
                position += 100 - num
            else:
                position = cur
                if position == 0:
                    res += 1
        else:
            cur = position + num
            if cur > 99:
                res += 1
                position += num - 100
            else:
                position = cur

    return res

print(count(test))
print(count(rows))