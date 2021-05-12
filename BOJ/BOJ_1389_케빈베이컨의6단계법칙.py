def dijkstra(user):
    dist = [99999999] * (N+1)
    visited = [False] * (N+1)

    dist[user] = 0

    for _ in range(N):
        min_dist = 99999999
        min_idx = -1

        # 모든 정점을 돌면서 최솟값 찾기
        for i in range(N+1):
            if not visited[i] and min_dist > dist[i] + 1:  # 방문하지 않았고, 제일 가까운 방법이라면
                min_dist = dist[i] + 1
                min_idx = i

        visited[min_idx] = True  # 방문체크

        # 현재 최솟값 기점으로 다시 모든 정점을 탐색
        for i in range(N+1):
            # 연결되어 있다면,
            if i in relations[min_idx]:
                if not visited[i] and dist[i] > dist[min_idx] + 1:  # 기존 값이 더 크다면
                    dist[i] = dist[min_idx] + 1  # 갱신

    return sum(dist[1:])


N, M = map(int, input().split())  # 유저 수/ 친구 관계 수

relations = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    if n2 not in relations[n1]:  # 이미 입력된 관계가 아닐 경우
        relations[n1].append(n2)  # 무향그래프 양쪽 등록
        relations[n2].append(n1)

min_value = 99999999
ans = 0

# 모든 정점을 기준으로 dijkstra 실행
for i in range(1, N+1):
    now_value = dijkstra(i)

    if now_value < min_value:
        min_value = now_value
        ans = i

print(ans)
