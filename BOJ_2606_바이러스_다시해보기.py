def dfs(v):
    global cnt

    visited[v] = True
    cnt += 1

    for each in linked[v]:  # v번 컴퓨터와 연결되어 있는 각 컴퓨터에 대해서
        if not visited[each]:  # 방문한 적이 없다면, dfs 시행
            dfs(each)


C = int(input())  # 컴퓨터의 수
N = int(input())  # 네트워크 수

linked = [[] for _ in range(C+1)]  # 1번부터 시작
for _ in range(N):
    c1, c2 = map(int, input().split())
    linked[c1].append(c2)  # 무향 == 양쪽 등록
    linked[c2].append(c1)

visited = [False] * (C+1)
cnt = -1  # 1번 컴퓨터는 계산하지 않습니다.

dfs(1)  # 1번 컴퓨터가 바이러스에 걸렸다.

print(cnt)