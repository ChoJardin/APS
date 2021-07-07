from collections import deque

def bfs():

    # 사방탐색
    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    queue = deque()
    queue.append((0, 0, 1))
    arr[0][0] = 0

    while queue:
        y, x, cnt = queue.popleft()

        if y == N-1 and x == M-1:
            print(cnt)
            return

        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            # 범위확인, 이동가능 여부 확인
            if -1 < move_y < N and -1 < move_x < M and arr[move_y][move_x]:
                # 이동가능하다면 큐에 추가
                queue.append((move_y, move_x, cnt+1))
                # 방문체크
                arr[move_y][move_x] = 0


N, M = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(N)]

bfs()
