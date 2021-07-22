import sys
input = sys.stdin.readline


N = int(input())  # 노드의 개수

parent = [None for _ in range(N+1)]  # 부모, 가중치 저장
child = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(N-1):
    v, u, w = map(int, input().split())  # 부모, 자식, 가중치

    parent[u] = ([v, w])
    child[v].append(u)

# 자식 가지고 있는 개수 만큼 이중리스트 길이를 만들어줍니다..
# 자식이 둘이 아닐 수 있음 주의!!!
length = [[0] * len(child[i]) for i in range(N+1)]

# 뒤에가 리프일 가능성이 크니까.. 뒤부터 확인해서 앞으로 가보겠습니다..
for i in range(N, 1, -1):
    # 부모노드
    p = parent[i][0]

    # 몇번째 자식인지 확인
    for j in range(len(child[p])):
        if child[p][j] == i:
            break

    # 단말노드인 경우 -> [0] 으로 값을 초기화
    if not length[i]:
        length[i] = [0]

    # 부모노의에 자기의 최댓값 + 가중치를 저장
    length[p][j] = max(length[i]) + parent[i][1]

max_length = []
for i in range(N+1):
    # 자식들 중 최댓값 2개를 더한 값 저장
    max_length.append(sum(sorted(length[i], reverse=True)[:2]))

print(max(max_length))




    