# 왜 부녀회장이 되어야 하나
# 왜 이 아파트 주민들은 최저 주거환경도 보장되지 않은 곳에 사는가
def keep_plus(k, n):
    if k == 0:  # 0층 확인하려고 함
        # print(n)
        return n

    elif n == 1:  # 1호실부터 존재
        # print(1)
        return 1

    else:
        # k층 n호실 == k-1층 n호실 + k층 n-1호실
        return keep_plus(k-1, n) + keep_plus(k, n-1)


T = int(input())

for tc in range(T):
    k = int(input())  # 층
    n = int(input())  # 호실

    ans = keep_plus(k, n)

    print(ans)