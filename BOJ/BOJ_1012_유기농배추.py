def dfs(y, x):
    global warm

    stack = []
    stack.append((y, x))

    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    while stack:
        y, x = stack.pop()
        farm[y][x] = 0  # 방문확인

        for d in range(4):
            moved_y = y + dy[d]
            moved_x = x + dx[d]

            # 범위 확인, 배추가 있다면,
            if -1 < moved_y < N and -1 < moved_x < M and farm[moved_y][moved_x]:
                stack.append((moved_y, moved_x))

    warm += 1


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())  # 가로, 세로, 배추의 개수

    farm = [[0] * M for _ in range(N)]

    for __ in range(K):
        x, y = map(int, input().split())
        # 배추 표시 == 1
        farm[y][x] = 1

    warm = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j]:
                dfs(i, j)

    print(warm)
