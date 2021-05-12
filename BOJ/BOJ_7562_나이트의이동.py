# from collections import deque  # 1.

def knight(board):
    if current == arrive:
        return 0

    # BFS
    # 한 자리에서 움직일 수 있는 장소 == 8 곳
    # 8곳을 이동하면서 만약 -1 이라면, 원래 자리보다 거리 +1 한 값을 넣어주고 queue에 추가하기
    # queue를 계속 돌면 되겠어

    # knight 이동 범주
    dy = [-1, -1, +1, +1, -2, -2, +2, +2]
    dx = [-2, +2, -2, +2, -1, +1, -1, +1]

    # queue = deque()  # 1.
    queue = []  # 2/3.
    now = 0  # 3.
    # current 부터 이동 시작
    # 시작 지점 == 거리 == 0
    board[current[0]][current[1]] = 0  # 방문쳌
    queue.append(current)

    while queue:
        # v = queue.popleft()  # 1.
        # v = queue.pop(0)  # 2.
        v = queue[now]  # 3.
        now += 1  # 3.

        for i in range(8):
            move_y = v[0] + dy[i]
            move_x = v[1] + dx[i]

            # 범위 확인하고
            # 방문쳌 하면서 queue에 더해줍니다.
            if -1 < move_y < L and -1 < move_x < L and board[move_y][move_x] == -1:
                if [move_y, move_x] == arrive:
                    return board[v[0]][v[1]] + 1
                else:
                    board[move_y][move_x] = board[v[0]][v[1]] + 1
                    queue.append([move_y, move_x])


T = int(input())

for tc in range(T):
    L = int(input())  # 체스판 한 변의 길이
    board =[[-1] * L for _ in range(L)]
    # print(board)

    current = list(map(int, input().split()))  # 현재위치
    arrive = list(map(int, input().split()))  # 목적지
    # print(current)
    # print(arrive)

    print(knight(board))


'''
deque를 사용했을 경우 가장 빠름 -> 1. 
리스트 queue와 원형 queue를 섞은 것 처럼 사용하는 경우 리스트 queue 보다는 빠름 -> 2. 
리스트 queue가 가장 느림 -> 3. 
'''


