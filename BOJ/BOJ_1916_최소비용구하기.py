import heapq
import sys
input = sys.stdin.readline


def dijkstra(depart, arrive):
    # 최소힙
    heap = []

    # 출발지를 힙에 추가
    heapq.heappush(heap, (0, depart))

    # 힙이 비어있지 않은 동안,
    while heap:
        # 힙에서 하나 꺼내서
        w, v = heapq.heappop(heap)

        # 아직 방문하지 않았다면 == 비용 갱신 이전
        if costs[v] == INF:
            # 비용 갱신
            costs[v] = w
            # 연결된 애들 힙에 넣어주기
            # 이때, 현재까지의 비용을 갱신해서 추가해준다.
            for (m, u) in bus[v]:
                heapq.heappush(heap, (w+m, u))

        # 도착지점까지의 비용을 찾은 경우, 반복 종료
        if costs[arrive] != INF:
            return


N = int(input())  # 도시의 개수
M = int(input())  # 버스의 대수

bus = [[] for _ in range(N+1)]
for _ in range(M):
    v, u, w = map(int, input().split())
    # 앞이 우선순위 -> 비용이 앞에 오도록
    bus[v].append((w, u))

depart, arrive = map(int, input().split())

INF = 9999999999
costs = [INF for _ in range(N+1)]

dijkstra(depart, arrive)

print(costs[arrive])

