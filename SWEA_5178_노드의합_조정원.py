# T = int(input())
#
# for tc in range(T):
#     N, M, L = map(int, input().split())
#     # 각 노드에 저장된 값
#     value = [0] * (N+1)
#     # 왼쪽자식/ 오른쪽자식
#     left = [0] * (N+1)
#     right = [0] * (N+1)
#
#     leaves = []  # 모르겠다 일단 리프 값도 저장해보자
#     for _ in range(M):
#         # 짝수면 왼쪽 자식,
#         # 홀수면 오른쪽 자식
#         node, num = map(int, input().split())
#
#         # 일단 노드 값을 저장해봅시다.
#         value[node] = num
#         leaves.append(node)
#
#         # 리프노드들은 자식이 없으니까 left, right를 -1로 설정해 봅시다.
#         left[node] = -1
#         right[node] = -1
#
#         if node % 2:  # 홀수라면
#             right[node//2] = node
#         else:
#             left[node//2] = node
#
#     # print(left, right, value)
#
#     # print(dir(list))
#     while leaves != [1]:
#         for leaf in leaves:
#             # 마지막 노드가 형제가 없다면,
#             # 그 노드는 리프노드
#             그 노드 값 == 부모 노드 값
#             if leaf == N:
#                 value[leaf//2] = value[leaf]
#                 leaves.remove(leaf)
#                 leaves.append(leaf//2)
#                 break
#
#             if not leaf % 2 and leaf+1 in leaves:  # 짝수이면서 하나 더 큰 값도 값이 있다면, 더해서 부모 값 해주기
#                 value[leaf//2] = value[leaf] + value[leaf+1]
#                 leaves.remove(leaf)
#                 leaves.remove(leaf+1)
#                 leaves.append(leaf//2)
#                 break
#
#     # print(value)  # 됐다!
#     print('#{} {}'.format(tc+1, value[L]))


def backorder(root):
    global value

    if root <= N:
        backorder(root*2)
        backorder(root*2+1)
        # 여기서 부모의 값을 찍어줍니다..
        if root*2 > N:
            pass
        else:
            # 자식 외동
            if root*2+1 > N:
                value[root] = value[root*2]
            else:  # 자식 형제
                value[root] = value[root*2] + value[root*2+1]
                # print(value)


T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())  # N = 노드의 개수, M = 리프노드 개수, L = 출력할 노드 번호

    value = [0] * (N+1)

    for _ in range(M):
        node, num = map(int, input().split())
        value[node] = num

    # 루트는 1
    backorder(1)

    print('#{} {}'.format(tc+1, value[L]))










