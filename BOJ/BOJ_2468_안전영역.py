from collections import deque

# 이건 DFS

N = int(input())
land = []
heights = []
for _ in range(N):
    each = list(map(int, input().split()))
    land.append(each)
    heights += each

heights = list(set(heights))
heights.sort(reverse=True)  # 높이 역순으로 정렬

# 각 높이별로 visited 생성해서
# 그냥 land 를 확인해서 높이보다 높으면 check 를 바꿔주고 -> 1 으로
# 1만 사방탐색하면서 cnt +1

# 사방탐색
dy = [-1, +1, 0, 0]
dx = [0, 0, -1, +1]

max_cnt = -99999999999
for height in heights:  # 각 높이마다
    stack = deque()
    check = [[0] * N for _ in range(N)]

    # 현재 높이 기준 높거나 같으면 1로 만든다.
    # 1만 돌면서 DFS로 확인할 것
    for i in range(N):
        for j in range(N):
            if land[i][j] >= height:
                check[i][j] = 1

    # DFS
    cnt = 0
    for i in range(N):
        for j in range(N):
            if check[i][j]:
                stack.append((i, j))

                while stack:
                    v = stack.pop()
                    now_y = v[0]
                    now_x = v[1]

                    # 방문쳌
                    check[now_y][now_x] = 0

                    for m in range(4):
                        move_y = now_y + dy[m]
                        move_x = now_x + dx[m]

                        if -1 < move_y < N and -1 < move_x < N and check[move_y][move_x]:
                            stack.append((move_y, move_x))

                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)

# print(safe())
# 입력 받은 다음에 최저~ 최고 높이를 확인하고,
# 최고부터 시작해서 stack에 집어넣으면서 사방탐색 본인보다 크다면 이동, 작다면 break 입니다.
# def safe():
#     global land, height
#     stack = deque()
#
#     # 사방탐색
#     dy = [-1, +1, 0, 0]
#     dx = [0, 0, -1, +1]
#     # 높은 곳부터 가져옵니다...
#     max_cnt = -999999
#     for height in heights:
#         visited = [[False] * N for _ in range(N)]
#         cnt = 0
#
#         for i in range(N):
#             for j in range(N):
#                 if land[i][j] > height:  # 더 높은 곳이라면, stack에 push 합니다.
#                     stack.append((i, j))
#
#                     while stack:
#                         v = stack.pop()
#                         now_y = v[0]
#                         now_x = v[1]
#
#                         visited[now_y][now_x] = True
#
#                         for m in range(4):
#                             move_y = now_y + dy[m]
#                             move_x = now_x + dx[m]
#
#                             # 더 높은 곳이면서, 방문하지 않은 곳이면
#                             # stack에 push 한다.
#                             if -1 < move_y < N and -1 < move_x < N:
#                                 if land[move_y][move_x] > height and not visited[move_y][move_x]:  # 높으면서 방문하지 않음
#                                     stack.append((move_y, move_x))
#                     cnt += 1
#         if max_cnt < cnt:
#             max_cnt = cnt
#
#     return max_cnt
