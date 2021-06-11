from collections import deque

def bfs(x, sec):  # 현재위치, 지금까지 몇초

    # 방문확인
    history = set()

    # 수빈이의 이동
    move = [-1, +1]

    queue = deque()
    queue.append((x, sec))

    while queue:
        x, sec = queue.popleft()

        # 동생 찾았다면,
        if x == K:
            return sec

        # 순간이동
        # 큐는 선입선출 -> 순간이동이 항상 한칸씩 이동하는 것보다 빠르기 때문에 앞에 두게 되면,
        # 무조건 동생을 처음 찾는 애가 가장 빨리 도달하는 애가 된다.
        move_x = 2 * x
        # 범위 확인
        if -1 < move_x < 100001:
            if not history.__contains__(move_x):
                queue.append((move_x, sec))
                history.add(move_x)

        # 한 칸 이동
        for i in range(2):
            move_x = x + move[i]

            # 범위 확인
            if -1 < move_x < 100001:
                if not history.__contains__(move_x):
                    queue.append((move_x, sec+1))
                    history.add(move_x)


N, K = map(int, input().split())

print(bfs(N, 0))
