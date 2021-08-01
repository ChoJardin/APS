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

# 나를 정점으로 자식노드에서 나한테 오는 길이 저장할 리스트
# 자식은 둘이 아닐 수 있음 주의!!!
length = [[0] * 2 for i in range(N+1)]

# 뒤에가 리프니까.. 뒤부터 확인해서 앞으로 가보겠습니다..
for i in range(N, 1, -1):
    # 부모노드
    p = parent[i][0]

    # 부모노드에 자기의 최댓값 + 가중치를 저장
    length[p].append(max(length[i]) + parent[i][1])
    # 어차피 최댓값 2개만 가지고 있으면 되는 걸..!
    length[p] = sorted(length[p], reverse=True)[:2]

print(max(map(sum, length)))


# 처음에는 노드의 자식들의 길이를 하나씩 다 저장하고 있었는데,
# 그러면 쓸데없는 반복
# -> 1. 몇번째 자식인지 알려고 for문 돌기
# -> 2. 최댓값 2개 뽑으려고 다시 for문 돌기
# 등등이 많아져서 시간이 매우 오래 걸렸습니다.
# 결국 지름은 자식 2개만 필요하니까 최댓값 2개만 가지고 있으면 되는 것이었어요.



    