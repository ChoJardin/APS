# 다익스트라
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):

    # 힙
    heap = []

    # 거리 초기화
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        # 가장 가중치 적은 애 pop
        w, v = heapq.heappop(heap)

        # 갈 수 있는 경로에서
        for uw, u in arr[v]:
            # 저장되어 있는 경로보다 더 가깝다면 -> 갱신
            if uw + w < distance[u]:
                distance[u] = uw + w
                heapq.heappush(heap, (uw+w, u))

        ### 시간초과
        # for uw, u in arr[v]:
        #     if uw + distance[v] < distance[u]:
        #         distance[u] = uw + distance[v]
        #         heapq.heappush(heap, (uw, v))



V, E = map(int, input().split())
start = int(input())
# 인접리스트
arr = [[] for _ in range(V+1)]
# 최단 거리 등록
INF = 9999999999
distance = [INF] * (V+1)

for _ in range(E):
    v, u, w = map(int, input().split())
    # 가중치 먼저 저장 -> 힙에서 먼저 오는 애가 우선
    # 유향
    arr[v].append((w, u))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

