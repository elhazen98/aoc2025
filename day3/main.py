with open("data.txt", encoding="utf-8") as f:
    rows = [line.strip() for line in f]

def count(nums, need):
    n = len(nums)
    digits = ["0"] * need
    for i, num in enumerate(nums):
        max_fill = min(need, n - i)
        cuted = False
        while len(digits) > 0 and num > digits[-1] and max_fill > 0:
            digits.pop()
            max_fill -= 1
            cuted = True
        if cuted:
            digits.append(num)
        digits += ["0"] * (need - len(digits))

    res = 0
    for num in digits:
        res = res * 10 + int(num)
    
    return res

def sumAll(rows):
    res = 0
    for row in rows:
        res += count(row, 12)
    
    return res

print(sumAll(rows))

    


    
    

