def make_one(num, cnt):
    global min_cnt

    if cnt >= min_cnt:
        return

    if num == 1:
        min_cnt = cnt
        return
    elif num == 2 or num == 3:
        min_cnt = cnt+1
        return

    if num % 2 == 0 and not visited.__contains__((num // 2, cnt+1)):
        visited.add((num // 2, cnt+1))
        make_one(num // 2, cnt + 1)
        # visited.add((num % 2, cnt + 1))
    if num % 3 == 0 and not visited.__contains__((num // 3, cnt+1)):
        visited.add((num // 3, cnt + 1))
        make_one(num // 3, cnt+1)
    if num > 1 and not visited.__contains__((num -1, cnt+1)):
        visited.add((num-1, cnt+1))
        make_one(num-1, cnt+1)


visited = set()
visited.add((1, 0))
visited.add((2, 1))
visited.add((3, 1))

min_cnt = 9999999999999

make_one(int(input()), 0)
print(min_cnt)
