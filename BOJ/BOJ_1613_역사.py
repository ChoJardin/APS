from collections import deque


def bfs(v, y, n):  # 시작정점, 도착정점, 무슨 리스트를 보겠니
    visited = [False] * (N+1)

    if n:
        link = arr_re
    else:
        link = arr

    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()

        for u in link[v]:
            if u == y:
                return True

            if not visited[u]:
                queue.append(u)
                visited[u] = True

    return False


N, K = map(int, input().split())  # 사건의 개수, 알고 있는 전후관계

# 인접리스트
arr = [[] for _ in range(N+1)]
arr_re = [[] for _ in range(N+1)]

for _ in range(K):
    x, y = map(int, input().split())
    arr[x].append(y)  # 유향그래프
    arr_re[y].append(x)  # 반방향도 기록

S = int(input())  # 알고 싶은 전후관계 개수
for _ in range(S):
    x, y = map(int, input().split())

    if bfs(x, y, 0):  # 도달했다 == x가 먼저 일어났다.
        print(-1)
    elif bfs(x, y, 1):  # 반대 순서로 일어났다
        print(1)
    else:  # 전후관계 파악이 불가능함
        print(0)


