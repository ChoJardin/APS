import sys
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

# 세로
for i in range(N):
    # 가로 -> 세로랑 같은 인덱스 까지만 확인
    for j in range(0, i+1):

        # 맨 위
        if i == 0 and j == 0:
            dp[i][j] = triangle[i][j]

        # 왼쪽 끝
        elif j == 0:
            dp[i][j] = dp[i-1][0] + triangle[i][j]

        # 오른쪽 끝
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]

        # 그 밖의 경우 -> 대각선 위 두개 비교해서 더 큰값 선택
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

print(max(dp[N-1]))





