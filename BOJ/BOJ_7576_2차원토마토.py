from collections import deque

def tomato():
    global tomatoes, M, N

    count_zero = False  # 익어야 하는 토마토가 하나도 없음
    queue = deque()  # BFS 시작점
    for y, line in enumerate(tomatoes):
        for x in range(M):
            if not line[x]:
                count_zero = True
            if line[x] == 1:
                queue.append((y, x))

    # 다 익어 있는 경우
    if not count_zero:
        return 0

    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    # 시작점을 가지고 사방탐색 시작
    while queue:
        v = queue.popleft()
        y = v[0]
        x = v[1]
        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            if -1 < move_y < N and -1 < move_x < M and not tomatoes[move_y][move_x]:
                tomatoes[move_y][move_x] = tomatoes[y][x] + 1
                queue.append((move_y, move_x))

    for y, line in enumerate(tomatoes):
        for x in range(M):
            if not line[x]:
                return -1

    return max(map(max, tomatoes)) - 1


M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
# print(tomatoes)

ans = tomato()
print(ans)
