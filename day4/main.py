with open("data.txt", encoding="utf-8") as f:
    origin = [line.strip() for line in f]
  
test = ["..@@.@@@@.", "@@@.@.@.@@", "@@@@@.@.@@", "@.@@@@..@.", "@@.@@@@.@@", ".@@@@@@@.@", ".@.@.@.@@@", "@.@@@.@@@@", ".@@@@@@@@.", "@.@.@@@.@."]

def count(grid):
    ROW = len(grid)
    COL = len(grid[0])
    DIR = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    matrix = [[1 if grid[i][j] == "@" else 0 for j in range(COL)] for i in range(ROW)]
    res = 0

    for row in range(ROW):
        for col in range(COL):
            if matrix[row][col] > 0:
                for r, c in DIR:
                    neir = row + r
                    neic = col + c
                    if 0 <= neir < ROW and 0 <= neic < COL and matrix[neir][neic] > 0:
                        matrix[row][col] += 1

    deleted = []
    for row in range(ROW):
        for col in range(COL):             
          if 0 < matrix[row][col] < 5:
              deleted.append([row, col])
              res += 1
              matrix[row][col] = 0

    while deleted:
        new_deleted = []
        for row, col in deleted:
            for r, c in DIR:
                neir = row + r
                neic = col + c
                if 0 <= neir < ROW and 0 <= neic < COL and matrix[neir][neic] > 0:
                    matrix[neir][neic] -= 1
                    if matrix[neir][neic] < 5:
                        new_deleted.append([neir, neic])
                        res += 1
                        matrix[neir][neic] = 0
        deleted = new_deleted

    return res

print(count(origin))
print(count(test))
