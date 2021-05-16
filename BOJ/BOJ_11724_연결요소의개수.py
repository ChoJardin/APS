import sys

def find_set(x):
    if P[x] != x:
        P[x] = find_set(P[x])
    return P[x]


def union(x, y):
    P[find_set(y)] = find_set(x)


N, M = map(int, input().split())  # 정점, 간선

# 서로소집합
P = [i for i in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    union(x, y)

# 강제로 모든 원소 한번씩 돌면서 대표 찾아주기
for i in range(N+1):
    find_set(i)

group = 0
cnt = N
for i in range(1, N+1):
    if P.count(i):
        cnt -= P.count(i)
        group += 1
    if not cnt:
        break

print(group)
