# 크루스칼
# 서로소집합
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)


N = int(input())  # 컴퓨터의 수
M = int(input())  # 연결할 수 있는 선의 수

# 간선 입력
edges = [list(map(int, input().split())) for _ in range(M)]
# 간선 오름차순 정렬
edges = sorted(edges, key=lambda x: x[2])

# 서로소집합 -> 자기 자신을 대표로
p = [i for i in range(N+1)]

cost = 0  # 비용
cnt = 0  # 선택된 간선의 개수
idx = 0  # 확인할 간선

while cnt < N-1:
    x = edges[idx][0]
    y = edges[idx][1]

    # 두 정점의 부모가 다르다면
    if find_set(x) != find_set(y):
        cost += edges[idx][2]  # 비용 추가
        cnt += 1  # 간선 개수 추가
        union(x, y)  # 두개 간선 연결

    # 다음 간선 보겠음
    idx += 1

print(cost)

