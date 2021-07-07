from collections import deque

import sys
input = sys.stdin.readline


def dfs(v):

    # 방문체크
    dfs_visited[v] = True
    print(v, end=' ')

    # 정점 v와 연결된 점들을 확인하면서
    for each in edges[v]:
        # 아직 방문하지 않았다면,
        if not dfs_visited[each]:
            dfs(each)


def bfs():

    queue = deque()
    queue.append(V)
    bfs_visited[V] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for each in edges[v]:
            if not bfs_visited[each]:
                queue.append(each)
                bfs_visited[each] = True


N, M, V = map(int, input().split())  # 정점의 개수, 간선의 개수, 탐색 시작 정점

# 인접리스트
# 정점은 1부터 시작 -> 인덱스 그대로 활용하기 위해 +1 해준다
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # 무향
    edges[a].append(b)
    edges[b].append(a)

# 여러개인 경우 정점 번호가 작은 순으로 방문 -> sort
for each in edges:
    each.sort()

# dfs
dfs_visited = [False for _ in range(N+1)]
dfs(V)

print()

# bfs
bfs_visited = [False for _ in range(N+1)]
bfs()




