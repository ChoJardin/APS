'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''


def inorder(root):
    global result

    if root <= V:
        inorder(root*2)
        result += value[root]
        inorder(root*2+1)


T = 10

for tc in range(10):
    V = int(input())

    value = [0] * (V+1)

    for _ in range(V):
        each = list(input().split())
        value[int(each[0])] = each[1]

    # 루트는 1이다.

    result = ''

    inorder(1)

    print('#{} {}'.format(tc+1, result))





