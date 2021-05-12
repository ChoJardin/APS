# BFS 로 이동하면서 거리를 저장합니다.
# 길마다 복구 시간이 다르기 때문에 가중치를 두면서 더해줍니다.

from collections import deque


def find_road():

    # 사방탐색
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    # BFS 합니다.
    queue = deque()
    queue.append((0, 0))
    # print(queue)

    while queue:
        v = queue.popleft()

        # 사방탐색하면서 이동해줍니다.
        for i in range(4):
            move_y = v[0] + dy[i]
            move_x = v[1] + dx[i]

            if -1 < move_y < N and -1 < move_x < N:  # 범위 안에 있으면서,
                if distance[move_y][move_x] > distance[v[0]][v[1]] + road[move_y][move_x]:  # 현재 저장된 거리보다 가깝다면
                    # 저장된 거리를 바꿔준다.
                    distance[move_y][move_x] = distance[v[0]][v[1]] + road[move_y][move_x]
                    # print(distance)
                    queue.append([move_y, move_x])


T = int(input())

for tc in range(T):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    # print(road)

    # 지도랑 같은 크기의 거리 체크 리스트 생성
    distance = [[9999999]*N for _ in range(N)]
    distance[0][0] = 0
    # print(distance)

    # 시작은 무조건 (0, 0)
    # 도착은 무조건 (N-1, N-1)
    find_road()

    print('#{} {}'.format(tc+1, distance[N-1][N-1]))




