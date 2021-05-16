def make_num(num):
    global cnt

    if num == 0:
        cnt += 1
        return

    # 들어온 숫자를 빼주면서 가겠습니다.
    if num >= 1:
        make_num(num-1)
    if num >= 2:
        make_num(num-2)
    if num >= 3:
        make_num(num-3)


T = int(input())

for _ in range(T):
    visited = set()
    cnt = 0
    num = int(input())

    make_num(num)

    print(cnt)
