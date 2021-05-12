from collections import deque


def bfs(v, sum_, direction):  # 기준점, 총액, 방향
    global _board, costs, N

    # 사방탐색
    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    queue = deque()
    queue.append((v, sum_, direction))
    costs[v[0]][v[1]] = 0

    while queue:
        (y, x), now_sum, now_dir = queue.popleft()

        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            # 범위확인/ 이동 가능함
            if -1 < move_y < N and -1 < move_x < N and _board[move_y][move_x] == 0:
                # 금액이랑.. 방향이랑 확인해서 코스트랑 비교해야 합니다...
                if now_dir == -1:  # 처음이라면,
                    queue.append(((move_y, move_x), now_sum + 100, i))
                    costs[move_y][move_x] = now_sum + 100

                # 동일한 금액인 경우에도 큐에 넣어서 확인이 필요합니다.
                # 왜냐하면 방향에 따라서 이동하는 자리에 찍히는 금액이 달라질 수도 있기 때문!
                elif now_dir in [0, 1]:  # 현재 방향 == 상/하
                    if i in [0, 1]:  # 같은 방향
                        if costs[move_y][move_x] >= now_sum + 100:  # 지금 이동하는 것 보다 더 비용 많이 들었음
                            # 갱신
                            costs[move_y][move_x] = now_sum + 100
                            queue.append(((move_y, move_x), costs[move_y][move_x], i))
                    else:  # 코너를 돌아야 한다.
                        if costs[move_y][move_x] >= now_sum + 600:  # 직선 + 코너 비용
                            costs[move_y][move_x] = now_sum + 600
                            queue.append(((move_y, move_x), costs[move_y][move_x], i))

                else:  # 좌/우
                    if i in [2, 3]:  # 같은 방향
                        if costs[move_y][move_x] >= now_sum + 100:  # 지금 이동하는 것 보다 더 비용 많이 들었음
                            # 갱신
                            costs[move_y][move_x] = now_sum + 100
                            queue.append(((move_y, move_x), costs[move_y][move_x], i))
                    else:  # 코너를 돌아야 한다.
                        if costs[move_y][move_x] >= now_sum + 600:  # 직선 + 코너 비용
                            costs[move_y][move_x] = now_sum + 600
                            queue.append(((move_y, move_x), costs[move_y][move_x], i))


def solution(board):
    global _board, costs, N

    N = len(board)  # N * N
    _board = board
    costs = [[99999999999999] * N for _ in range(N)]  # 방문확인

    bfs((0, 0), 0, -1)  # 시작점, 방향

    return costs[N-1][N-1]
