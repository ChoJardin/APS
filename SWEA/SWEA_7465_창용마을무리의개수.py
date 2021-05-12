T = int(input())

for tc in range(T):
    N, M = map(int, input().split())  # 정점/ 관계

    linked_list = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        linked_list[u].append(v)
        linked_list[v].append(u)

    def dfs(v):
        global visited
        visited[v] = True

        for w in linked_list[v]:
            if not visited[w]:
                dfs(w)

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt +=1
            dfs(i)

    print('#{} {}'.format(tc+1, cnt))


