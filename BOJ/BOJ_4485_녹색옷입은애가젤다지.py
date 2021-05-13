from collections import deque

def bfs():
    cost = [[9999999999] * N for _ in range(N)]

    # 사방탐색
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    queue = deque()
    # 항상 0, 0 에서 시작한다.
    queue.append((0, 0))
    cost[0][0] = arr[0][0]  # 방문쳌/ 비용 저장

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            # 범위확인 & 지금이 최소비용이라면,
            if -1 < move_y < N and -1 < move_x < N and cost[move_y][move_x] > arr[move_y][move_x] + cost[y][x]:
                # 갱신
                cost[move_y][move_x] = arr[move_y][move_x] + cost[y][x]
                queue.append((move_y, move_x))

    # 다 끝났으면 최소비용이 저장되어있다.
    return cost[N-1][N-1]


tc = 1
while True:

    N = int(input())
    if not N:  # 0이면 반복 종료
        break

    # 도둑루피 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'Problem {tc}: {bfs()}')
    tc += 1



