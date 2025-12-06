with open("data.txt", encoding="utf-8") as f:
    origin = [line.strip() for line in f]

test = ["123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  "]


def count(data):
    row = len(data) - 1
    nums = [[int(n) for n in num.split()] for num in data[:len(data) - 1]]
    oper = [sym for sym in data[-1].split()]

    res = 0
    for c, o in enumerate(oper):
        if o == "+":
            cur = 0
            for r in range(row):
                cur += nums[r][c]
            res += cur
        else:
            cur = 1
            for r in range(row):
                cur *= nums[r][c]
            res += cur

    return res


def count2(data):
    row = len(data) - 1
    rev = [d[::-1] for d in data]
    oper = [sym for sym in rev[-1].split()]

    res = 0
    o = 0
    c = 0
    cur_tot = 0 if oper[o] == "+" else 1
    while o < len(oper) and c < len(data[0]):
        cur_num = 0
        for r in range(row):
            if rev[r][c] == " ":
                continue
            cur_dig = int(rev[r][c])
            cur_num = cur_num * 10 + cur_dig
        if cur_num > 0:
            if oper[o] == "+":
                cur_tot += cur_num
            else:
                cur_tot *= cur_num
        else:
            res += cur_tot
            o += 1
            cur_tot = 0 if oper[o] == "+" else 1
        c += 1

    return res + cur_tot


print(count2(test))
print(count2(origin))
