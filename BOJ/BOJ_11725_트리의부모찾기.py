import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

# 인접리스트
# 무향
nodes = [[] for _ in range(N+1)]

for _ in range(N-1):
    v, u = map(int, input().split())
    nodes[v].append(u)
    nodes[u].append(v)

tree = [False] * (N+1)  # 1번부터 사용

queue = deque()  # 확인할 노드 번호 저장

# 1번 노드가 루트노드
tree[1] = -1
for each in nodes[1]:
    queue.append(each)
    tree[each] = 1

while queue:
    # 연결된 원소부분 확인하면서, 앞에서 온 곳을 올려준다.
    v = queue.popleft()

    for each in nodes[v]:
        if not tree[each]:  # 아직 부모 확인되지 않았음
            tree[each] = v
            queue.append(each)

for i in range(2, N+1):
    print(tree[i])


