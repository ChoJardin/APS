# 크기가 N * N 인 체스판 위에
# 퀸 N 개를 서로 공격할 수 없게 놓는 문제
# 교수님의 소중한 힌트
"""
NQueen은
퀸의 공격범위 : 8 방향
그게 가로도 포함이기 떄문에
한 행에는 하나씩만 놓고
다음으로 내려간다.
해당 자리가 놓을 수 있는 자리인지를 체크 한다음에 놓고 내려가야 한다.
놓는다는 것 : 실제 맵상에 표시 or visited check
"""

def queen(row):
    global board, ans

    # 퀸이 움직일 수 있는 8 방향
    # 근데 팔방탐색이 필요가 없습니다.. 왜냐면 앞으로 아래쪽으로만 놓을 거라서요..
    dy = [+1, +1, +1]
    dx = [0, +1, -1]

    if row == N:
        ans += 1
        return

    for i in range(N):  # 처음 칸 부터 순서대로 놓는다.
        if not board[row][i]:  # 놓을 수 있는 자리라면
            board[row][i] = 1

            # 저기 기점으로 퀸의 이동 가능 공간을 찍어준다.
            for j in range(3):
                move_y = row + dy[j]
                move_x = i + dx[j]

                while -1 < move_y < N and -1 < move_x < N:
                    board[move_y][move_x] += 1
                    move_y = move_y + dy[j]
                    move_x = move_x + dx[j]

            # for each in board:
            #     print(each)
            # print('')

            # 이제 퀸이 방문할 수 없는 자리에 다음줄에 놓아주면 되는 것이다.
            queen(row+1)

            # 돌아오면 초기화가 필요함
            board[row][i] = 0
            for j in range(3):
                move_y = row + dy[j]
                move_x = i + dx[j]

                while -1 < move_y < N and -1 < move_x < N and board[move_y][move_x]:
                    board[move_y][move_x] -= 1  # 갈 수 없는 칸이 중복될 수 있기 때문에 더해주고 빼준다.
                    move_y = move_y + dy[j]
                    move_x = move_x + dx[j]



N = int(input())

# 퀸은 상하좌우대각선 아무렇게나 다 움직일 수 있다.
# 퀸을 첫째 줄에 0부터 순서대로 놓고,
# 8방향 전부를 방문쳌
# 다음 줄 그리고 방문 되어 있지 않은 곳에 퀸을 놓고, 다시 방문 쳌
# 마지막 줄 까지 다 했으면, +1 하고, 다음 경우의 수 확인 이렇게 인가요...

board = [[0] * N for _ in range(N)]
ans = 0

queen(0)

print(ans)
