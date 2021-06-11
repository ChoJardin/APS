import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
# 해당 열 까지의 합을 저장하는 리스트
sum_arr = [[0] * (N+1) for _ in range(N+1)]

# 세로
for i in range(N+1):
    # 가로
    for j in range(N+1):
        if i == 0 or j == 0:
            continue

        else:
            # [i-1]까지의 가로합 + [j-1]까지의 세로합 - 중복([i-1][j-1]) + 해당 위치
            sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1] + arr[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1])



