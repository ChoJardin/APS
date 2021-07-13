# DP

import sys
input = sys.stdin.readline


T = int(input())

for tc in range(T):
    N = int(input())

    stickers = [list(map(int, input().split())) for _ in range(2)]

    # 해당 행의 스티커를 선택했을 때,
    # 해당 열까지의 최댓값
    # 모두 0으로 초기화
    dp = [[0] * (N+1) for _ in range(3)]

    # 가로
    for i in range(1, N+1):
        # 세로
        for j in range(1, 3):

            # 맨 첫 열의 경우, 일단 선택한다.
            if i == 1:
                dp[j][i] = stickers[j-1][i-1]
                continue

            # 첫 열이 아닌 경우,
            # 각 행에 따라 경우의 수 고려
            # 1 행을 선택할 수 있는 경우
            #   1. 직전 열에서 아무 스티커도 선택하지 않음,
            #   2. 직전 열에서 2행의 스티커를 선택한 경우
            # 위의 경우 중 최댓값 + 현재 행을 선택하는 경우의 스티커 값
            if j == 1:
                dp[j][i] = max(dp[1][i-2], dp[2][i-2], dp[2][i-1]) + stickers[j-1][i-1]

            elif j == 2:
                dp[j][i] = max(dp[1][i-2], dp[2][i-2], dp[1][i-1]) + stickers[j-1][i-1]

    # dp의 최댓값 출력
    print(max(map(max, dp)))