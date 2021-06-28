import sys
input = sys.stdin.readline

N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]
# print(costs)

# 가로 -> 색칠되는 인덱스
# 세로 -> 0, R, G, B
colors = [list(0 for i in range(N+1)) for _ in range(4)]

for i in range(N+1):
    for j in range(4):
        if not i or not j:
            colors[j][i] = 0

        else:
            # R
            # 여기서 R로 색칠되기 위해서는 이전에 R이 아니라 다른 색으로 칠해져 있으면 된다.
            if j == 1:
                colors[j][i] = min(colors[2][i-1], colors[3][i-1]) + costs[i-1][0]
            # G
            elif j == 2:
                colors[j][i] = min(colors[1][i-1], colors[3][i-1]) + costs[i-1][1]
            # B
            elif j == 3:
                colors[j][i] = min(colors[1][i-1], colors[2][i-1]) + costs[i-1][2]

# print(colors)

print(min(colors[1][N], colors[2][N], colors[3][N]))
