# 아무 정점에서나 시작해서 가장 먼 정점을 찾고
# 그 정점에서 다시 가장 먼 정점을 찾으면
# 그게 트리의 지름이 된다.

from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(v):

    INF = 999999999999
    min_dist = [INF for _ in range(N+1)]

    heap = []

    for each in tree[v]:
        heappush(heap, each)
    min_dist[v] = (0, v)

    while heap:
        w1, u = heappop(heap)
        if min_dist[u] == INF:
            min_dist[u] = (w1, u)

            for w2, u2 in tree[u]:
                heappush(heap, [w1+w2, u2])

    # print(min_dist)
    return max(min_dist[1:], key=lambda x: x[0])


N = int(input())

tree = [[] for _ in range(N+1)]
link = dict()

for i in range(1, N+1):
    sub = list(map(int, input().split()))
    v = sub[0]
    sub = sub[1:-1]
    for j in range(0, len(sub), 2):
        u, w = sub[j], sub[j+1]
        tree[v].append([w, u])

# 1번부터 가장 먼 정점
max_1, v1 = dijkstra(1)
# 가장 먼 정점부터 제일 먼 정점
max_2, v2 = dijkstra(v1)

print(max_2)

