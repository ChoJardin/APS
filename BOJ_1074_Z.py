def find_order(N, check, cnt, r, c):  # 배열 전체 크기, 몇번째 확인, 이제까지 확인한 횟수, 찾는 값 == (r, c)
    global total_cnt

    # 마지막 확인
    if check == 1:
        if r == 0:
            if c == 0:
                pass
            else:
                cnt += 1
        else:
            if c == 0:
                cnt += 2
            else:
                cnt += 3

        total_cnt = cnt
        return

    mid = (2**check-1)//2  # 중간값 == 어느 사분면을 확인할지의 기준
    one_range = 4**(check-1)  # 한 사분면 전체를 지나는 경우 확인하는 개수
    if r > mid:  # 3, 4 사분면
        if c > mid:  # 4 사분면
            cnt += one_range * 3  # 1, 2, 3 사분면을 전부 확인하고 온다.
            find_order(N, check-1, cnt, r - 2**(check-1), c - 2**(check-1))  # 사분면의 크기가 줄어드는 만큼 찾는 위치를 변경해 준다.

        else:  # 3 사분면
            cnt += one_range * 2
            find_order(N, check-1, cnt, r - 2**(check-1), c)

    else:  # 1, 2 사분면
        if c > mid:  # 2 사분면
            cnt += one_range
            find_order(N, check-1, cnt, r, c - 2**(check-1))

        else:  # 1 사분면
            find_order(N, check-1, cnt, r, c)


N, r, c = map(int, input().split())  # 2**N/ (r, c)

total_cnt = 0
find_order(N, N, 0, r, c)

print(total_cnt)


