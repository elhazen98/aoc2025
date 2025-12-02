with open("data.txt", encoding="utf-8") as f:
    text = f.read().strip()

nums = [r.split("-") for r in text.split(",")]
test = [["38593856", "38593862"]]

def count(nums):
    all_range = []
    for start, finish in nums:
        n = len(start)
        if n % 2 == 1:
            first = ("1" + "0" * ((n + 1) // 2 - 1))
        else:
            first = start[:n//2]
            if first * 2 < start:
                first = str(int(first) + 1)
        
        if int(first * 2) > int(finish):
            continue
        
        m = len(finish)
        if m % 2 == 1:
            last = "9" * ((m - 1) // 2)
        else:
            last = finish[:m//2]
            if last * 2 > finish:
                last = str(int(last) - 1)
        
        all_range.append([first, last])
    
    res = 0
    for first, last in all_range:
        if first == last:
            res += int(first + last)
        else:
            while len(first) < len(last):
                cur_last = int(9 * len(first))
                cur_first = int(first)
                res += ((cur_last + cur_first) * (cur_last - cur_first + 1) // 2) * (10 ** len(first) + 1)    
                first = str(10 ** (len(first) + 1))
            length = len(first)
            last = int(last)
            first = int(first)
            cur = ((last + first) * (last - first + 1) // 2) * (10 ** length + 1)
            res += cur
    
    return res

def count2(nums):
    all_range = []
    for start, finish in nums:
        len_start = len(start)
        len_finish = len(finish)
        for digit in range(1, 6):
            need = digit - (len_start % digit) if len_start % digit > 0 else 0
            times_first = max((len_start + need) // digit, 2)
            if need > 0:
                first =  "1" + "0" * (digit - 1)
            else:
                first = start[:digit]
                if first * times_first < start:
                    first = str(int(first) + 1)
            
            if int(first * times_first) > int(finish):
                continue

            cut = len_finish % digit
            times_last = len_finish // digit
            if cut > 0:
                last = "9" * digit
            else:
                last = finish[:digit]
                if last * times_last > finish:
                    if last != "1":
                        last = str(int(last) - 1)
                    else:
                        last = "9"
                        times_last -= 1 

            all_range.append([first, times_first, last, times_last])
    
    visited = set()
    tot = 0
    for first, times_first, last, times_last in all_range:
        if times_first != times_last:
            cur1 = first * times_first
            if cur1 not in visited:
                visited.add(cur1)
                tot += int(cur1)
            cur2 = last * times_last
            if cur2 not in visited:
                visited.add(cur2)
                tot += int(cur2)
        else:
            for i in range(int(first), int(last) + 1):
                cur = str(i) * times_first
                if cur not in visited:
                    visited.add(cur)
                    tot += int(cur)
    
    return tot

print(count2(nums))
    




