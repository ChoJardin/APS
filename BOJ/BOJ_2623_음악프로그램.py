from collections import deque

N, M = map(int, input().split())  # 가수, 보조pd

# 진입차수 기록
in_degree = [0] * (N+1)
in_degree[0] = -1  # 사용 안 할 것..
# 연결 기록
arr = [[] for _ in range(N+1)]

for _ in range(M):
    order = list(map(int, input().split()))
    s = order[0]
    for i in range(1, s):
        arr[order[i]].append(order[i+1])  # 유향그래프
        in_degree[order[i+1]] += 1  # 진입차수 기록..

queue = deque()
for i in range(1, N+1):
    if not in_degree[i]:  # 진입차수가 없다면,
        queue.append(i)

results = []
while queue:
    v = queue.popleft()
    results.append(v)

    # 연결된 애들의 진입차수를 하나씩 빼준다.
    for singer in arr[v]:
        in_degree[singer] -= 1

        if not in_degree[singer]:
            queue.append(singer)

if len(results) != N:
    print(0)
else:
    for each in results:
        print(each)
