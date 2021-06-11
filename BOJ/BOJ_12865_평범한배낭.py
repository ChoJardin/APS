import sys
input = sys.stdin.readline

N, K = map(int, input().split())
goods = [tuple(map(int, input().split())) for _ in range(N)]  # 무게, 가치

# dp
# 세로 => 담을 수 있는 물건의 개수
# 가로 => 담을 수 있는 무게의 최대
dp = [[0 for i in range(K+1)] for j in range(N+1)]  # 가치의 최대 저장

# 각 물건의 개수
for i in range(N + 1):
    # 담을 수 있는 무게
    for j in range(K + 1):
        # 하나도 담을 수 없다.
        if not i or not j:
            continue

        # i-1번째의 무게가 j 보다 작은 경우
        elif goods[i-1][0] <= j:
            # 선택하거나
            select = dp[i-1][j-goods[i-1][0]] + goods[i-1][1]
            # 선택하지 않거나
            not_select = dp[i-1][j]
            # 둘 중 가치의 최댓값을 선택
            dp[i][j] = max(select, not_select)

        # i-1 번째의 무게가 j를 넘어가는 경우 -> 애초에 선택할 수가 없다.
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
