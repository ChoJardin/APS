from collections import deque

def bfs(v):
    # 사방탐색
    dy = [+1, 0]
    dx = [0, +1]

    queue = deque()
    queue.append(v)
    distance[v[0]][v[1]] = arr[v[0]][v[1]]

    while queue:
        now = queue.popleft()
        y = now[0]
        x = now[1]

        for i in range(2):
            move_y = y + dy[i]
            move_x = x + dx[i]

            if -1 < move_y < N and -1 < move_x < N and distance[move_y][move_x] > distance[y][x] + arr[move_y][move_x] and (move_y, move_x) != v:
                queue.append((move_y, move_x))
                distance[move_y][move_x] = distance[y][x] + arr[move_y][move_x]


T = int(input())

for tc in range(T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[9999999999] * N for _ in range(N)]
    # print(arr)

    # 출발지점 == (0, 0) // 도착지점 == (n-1, n-1)
    # bfs/ 거리저장합니다.

    bfs((0, 0))
    # print(distance)

    print('#{} {}'.format(tc+1, distance[N-1][N-1]))
