# 중위순회하면 된다.
def inorder(root):
    global value, cnt

    if root <= N:
        inorder(root*2)
        value[root] = cnt
        cnt += 1
        inorder(root*2+1)


T = int(input())

for tc in range(T):
    N = int(input())

    value = [0] * (N+1)
    cnt = 1

    inorder(1)

    print('#{} {} {}'.format(tc+1, value[1], value[N//2]))

