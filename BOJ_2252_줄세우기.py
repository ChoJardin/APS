from collections import deque

N, M = map(int, input().split())  # 학생 수, 누가 먼저

in_ = [0] * (N+1)  # 진입차수 기록
in_[0] = -1  # 사용하지 않을 값은 -1로 초기화

# 인접 리스트
linked = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    linked[a].append(b)  # 연결되어 있다.
    in_[b] += 1  # 진입차수 기록


queue = deque()
for i in range(N+1):
    if not in_[i]:  # 진입차수 0이라면,
        queue.append(i)

result = []
while queue:
    v = queue.popleft()
    result.append(v)

    for each in linked[v]:
        in_[each] -= 1  # 진입차수 하나 깎고
        if not in_[each]:  # 0이 되었으면,
            queue.append(each)

print(*result)

