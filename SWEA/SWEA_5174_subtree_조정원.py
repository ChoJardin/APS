# 전위로 하겠다
def preorder(root):
    global cnt

    if not root:
        return
    else:
        cnt += 1

    preorder(left[root])
    preorder(right[root])


T = int(input())

for tc in range(T):
    E, N = map(int, input().split())  # E == 간선 개수 근데 N은 무엇 == N 번째를 루트로 하는 트리
    tree = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(0, E*2, 2):

        if not left[tree[i]]:
            left[tree[i]] = tree[i+1]

        else:
            right[tree[i]] = tree[i+1]

    # print(left, right)

    # 루트 == N
    cnt = 0

    preorder(N)

    print('#{} {}'.format(tc+1, cnt))
