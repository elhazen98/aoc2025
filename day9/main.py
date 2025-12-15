with open("data.txt", encoding="utf-8") as f:
    origin = [line.strip() for line in f]

origin = [[int(n) for n in num.split(",")] for num in origin]

test = [[7, 1],
        [11, 1],
        [11, 7],
        [9, 7],
        [9, 5],
        [2, 5],
        [2, 3],
        [7, 3]]


def count(data):
    max_rec = 0
    length = len(data)
    for i in range(length):
        x1, y1 = data[i]
        for j in range(i + 1, length):
            x2, y2 = data[j]
            max_rec = max(max_rec, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

    return max_rec


def count2(data):
    length = len(data)
    v_line = []
    h_line = []
    for i in range(length):
        x1, y1 = data[i]
        x2, y2 = data[(i + 1) % length]
        if x1 == x2:
            v_line.append([x1] + sorted([y1, y2]))
        elif y1 == y2:
            h_line.append(sorted([x1, x2]) + [y1])

    max_rec = 0
    for i in range(length - 1):
        x1, y1 = data[i]
        for j in range(i + 1, length):
            x2, y2 = data[j]

            left = [x1] + sorted([y1, y2])
            top = sorted([x1, x2]) + [y1]
            right = [x2] + sorted([y1, y2])
            bot = sorted([x1, x2]) + [y2]

            if is_out(x1, y2, v_line, h_line):
                continue
            if is_out(x2, y1, v_line, h_line):
                continue
            if is_cut_h(left, h_line):
                continue
            if is_cut_v(top, v_line):
                continue
            if is_cut_h(right, h_line):
                continue
            if is_cut_v(bot, v_line):
                continue

            max_rec = max(max_rec, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

    return max_rec


def is_out(x_node, y_node, v_line, h_line):
    for x, y1, y2 in v_line:
        if x == x_node and y1 <= y_node <= y2:
            return False
    for x1, x2, y in h_line:
        if y == y_node and x1 <= x_node <= x2:
            return False

    cut = True
    for x, y1, y2 in v_line:
        if x > x_node and y1 <= y_node < y2:
            cut = not cut

    return cut


def is_cut_v(line, v_line):
    x1, x2, y = line
    for x, y1, y2 in v_line:
        if x1 < x < x2 and y1 < y < y2:
            return True

    return False


def is_cut_h(line, h_line):
    x, y1, y2 = line
    for x1, x2, y in h_line:
        if x1 < x < x2 and y1 < y < y2:
            return True

    return False


print(count2(test))
print(count2(origin))
