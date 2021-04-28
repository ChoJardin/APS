# 위상정렬
from collections import deque

T = 10

for tc in range(T):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    work = [0] * (V+1)  # 진입차수 기록할 리스트
    linked = [[] for _ in range(V+1)]  # 인접리스트

    ans = []

    for i in range(0, E*2, 2):
        work[arr[i+1]] += 1  # 진입차수 기록
        linked[arr[i]].append(arr[i+1])

    queue = deque()
    for idx, each in enumerate(work):
        if not each and idx:  # 진입차수가 0이고, 맨 앞의 0 제외
            queue.append(idx)  # 노드를 큐에 추가
    # print(queue)

    while queue:  # 큐가 빌 때 까지
        v = queue.popleft()
        ans.append(v)

        for each in linked[v]:  # 연결된 각 점들에 대해서
            work[each] -= 1  # 진입차수 1씩 감소
            if not work[each]:  # 진입차수가 0이되면
                queue.append(each)  # 해당 노드를 큐에 추가

    print('#{} {}'.format(tc+1, ' '.join(list(map(str, ans)))))

