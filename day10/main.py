with open("data.txt", encoding="utf-8") as f:
    origin = [line.strip() for line in f]

test = ["[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"]


def fix(data):

    def ints_to_dec(nums):
        dec = 0
        nums = [int(num) for num in nums[1:(len(nums) - 1)].split(",")]
        for num in nums:
            dec += 2 ** num

        return dec

    def light_to_dec(lights):
        dec = 0
        lights = lights[1:(len(lights) - 1)]
        for i in range(len(lights)):
            if lights[i] == "#":
                dec += 2 ** i

        return dec

    data = [[item for item in row.split(" ")] for row in data]
    for i, row in enumerate(data):
        light = light_to_dec(row[0])
        buttons = [ints_to_dec(nums) for nums in row[1:len(row) - 1]]
        joltages = [int(item)
                    for item in row[-1][1:(len(row[-1]) - 1)].split(",")]

        data[i] = [light, buttons, joltages]

    return data


def find_minimum(target, nums):

    def dfs(i, n, cur):
        if cur == target:
            return n
        if i >= len(nums):
            return float("inf")

        num = nums[i]
        cur_xor = cur ^ num

        return min(dfs(i + 1, n, cur), dfs(i + 1, n + 1, cur_xor))

    return dfs(0, 0, 0)


def count(data):
    data = fix(data)
    res = 0
    for row in data:
        target = row[0]
        nums = row[1]
        cur = find_minimum(target, nums)
        res += cur

    return res


# print(count(test))
# print(count(origin))


def fix2(data):

    def nums_to_grid(nums, light_len):
        nums = [int(num) for num in nums[1:(len(nums) - 1)].split(",")]
        grid = [0] * light_len
        for num in nums:
            grid[num] = 1

        return grid

    data = [[item for item in row.split(" ")] for row in data]
    matrix = []
    for i, row in enumerate(data):
        light = row[0][1:(len(row[0]) - 1)]
        buttons = [nums_to_grid(nums, len(light))
                   for nums in row[1:len(row) - 1]]
        joltages = [int(item)
                    for item in row[-1][1:(len(row[-1]) - 1)].split(",")]

        matrix_raw = sorted(buttons) + [joltages]
        matrix_row = []
        for j in range(len(light)):
            local_row = []
            for row in matrix_raw:
                local_row.append(row[j])
            matrix_row.append(local_row)

        matrix.append(matrix_row)

    return matrix


test2 = fix2(test)
for row in test2:
    print(row)
