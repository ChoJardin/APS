# 그냥 평범한 BFS 아닌가요?
# 왜 골드 5?

from collections import deque

def find_land():
    lands = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
              lands.append((i, j))
    return lands


def bfs(v):
    # 각 기준점을 가지고
    distance = [[0] * M for _ in range(N)]

    # 사방탐색
    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    queue = deque()
    queue.append(v)

    while queue:
        now = queue.popleft()
        y = now[0]
        x = now[1]

        # 사방탐색
        for i in range(4):
            move_y = now[0] + dy[i]
            move_x = now[1] + dx[i]

            # 범위 확인 // 땅인가? // 이미 갔는가? // 시작점이 아닌가?
            if -1 < move_y < N and -1 < move_x < M and arr[move_y][move_x] == 'L' and not distance[move_y][move_x] and (move_y, move_x) != v:
                # 큐에 올려줘
                queue.append((move_y, move_x))
                # 방문쳌 == 거리 등록
                distance[move_y][move_x] = distance[y][x] + 1

    return distance


N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
# print(arr)

lands = find_land()

max_distance = -99999999
for land in lands:

    # bfs 실행의 결과 == 그 땅으로부터 이동가능한 지점과의 거리
    result = bfs(land)

    now_max = max(map(max, result))  # 현재 land 에서의 최댓값

    if now_max > max_distance:  # 최대거리랑 현재 지점에서의 최대거리 비교
        max_distance = now_max

print(max_distance)

