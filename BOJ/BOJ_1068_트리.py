# 자식 노드 순회
def find_child(n):
    tree[n].append(-1)
    # 각 자식을 방문하면서
    for each in tree[n]:
        if each != -1:
            find_child(each)


N = int(input())

# 자식 노드를 저장한다.
tree = [[] for _ in range(N)]
root = -1
for (idx, each) in enumerate(list(map(int, input().split()))):
    # 루트가 아니라면,
    # 자식노드로 저장
    if each != -1:
        tree[each].append(idx)
    # 루트 저장
    else:
        root = idx

to_delete = int(input())

# 트리 순회하면서,
# 지워지는 노드부터 시작해서 자식 찾아가서 전부 -1 추가해준다
find_child(to_delete)

# 그 부모노드에서는 자식 노드 중에서 없애버린다.
# 하면서 리프인지도 확인해보자
leaf = 0
for each in tree:
    if not len(each):
        leaf += 1

    elif each.__contains__(to_delete):
        each.remove(to_delete)
        if not len(each):
            leaf += 1

print(leaf)




