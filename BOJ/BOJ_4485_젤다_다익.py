import heapq

def dijkstra():
    # 현재까지의 최소비용 == 매우 큰 값으로 설정
    cost = [[9999999999] * N for _ in range(N)]

    # 사방탐색
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    heap = []
    # (0, 0) 에서 시작
    heapq.heappush(heap, (arr[0][0], 0, 0))  # 현재까지 비용, y, x
    cost[0][0] = arr[0][0]

    while heap:
        w, y, x = heapq.heappop(heap)

        # 갈 수 있는 곳 확인해본다.
        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            # 범위 확인, 방문 여부 확인 -> 다익스트라의 경우 처음 방문이 무조건 최소..
            if -1 < move_y < N and -1 < move_x < N and cost[move_y][move_x] == 9999999999:
                cost[move_y][move_x] = w + arr[move_y][move_x]  # 비용 갱신
                heapq.heappush(heap, (cost[move_y][move_x], move_y, move_x))  # 힙푸쉬

    return cost[N-1][N-1]


tc = 1
while True:

    N = int(input())
    if not N:  # 0이면 반복 종료
        break

    # 도둑루피 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'Problem {tc}: {dijkstra()}')
    tc += 1
