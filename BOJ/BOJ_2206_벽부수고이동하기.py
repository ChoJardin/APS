from collections import deque

def bfs():
    global dist

    queue = deque()

    # 델타이동 -> 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    # 시작은 (1, 1)
    dist_false[0][0] = 1
    dist_true[0][0] = 1
    queue.append((0, 0, 1, False))  # 시작 정점, dist, 벽 부쉈나

    while queue:
        y, x, distance, is_broken = queue.popleft()

        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            # 범위 확인
            if -1 < move_y < N and -1 < move_x < M:
                # 벽을 부쉈을 때
                if is_broken:
                    # 벽이 아니면서 지금 가는 경로가 더 짧다면 갱신
                    if not arr[move_y][move_x] and dist_true[move_y][move_x] > distance + 1:
                        dist_true[move_y][move_x] = distance + 1
                        queue.append((move_y, move_x, distance+1, is_broken))

                # 벽을 아직 부순 적이 없을 때
                else:
                    # 벽일 때:
                    if arr[move_y][move_x]:
                        # 지금 가는 길이 더 짧은 경로라면, 부숴본다.
                        if dist_true[move_y][move_x] > distance + 1:
                            dist_true[move_y][move_x] = distance + 1
                            queue.append((move_y, move_x, distance+1, True))

                    # 벽이 아닐 때:
                    elif not arr[move_y][move_x] and dist_false[move_y][move_x] > distance + 1:
                        dist_false[move_y][move_x] = distance + 1
                        queue.append((move_y, move_x, distance+1, is_broken))


N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

# 거리정보 저장
# 벽을 부순 적이 없을 때
dist_false = [[9999999] * M for _ in range(N)]
# 벽을 부섰을 때
dist_true = [[9999999] * M for _ in range(N)]


bfs()

ans = min(dist_false[N-1][M-1], dist_true[N-1][M-1])
print(-1 if ans == 9999999 else ans)

