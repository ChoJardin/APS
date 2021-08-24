# import sys
# sys.stdin = open('SWEA_1953_input.txt', 'r')

from collections import deque

def bfs(r, c, L):
    ans = 0

    # r, c 자리에서 시작해서,
    # 델타탐색으로 이동가능여부 확인하고,
    # underground 이동하면서 이동한 곳은 9로 바꿔주고, -> 원본을 유지하고 있을 이유가 없음
    # 이동했으면 +1 해주고 마지막에 값 return

    # 현재 위치에서 이동가능한 구조가 어떻게 되는지 알아야 합니다.
    # 1 -> 위 2, 5, 6/ 아래 2, 4, 7/ 왼쪽 3, 4, 5/ 오른쪽 3, 6, 7
    # 2 -> 아래 4, 7/ 위 5, 6
    # 3 -> 왼쪽 4, 5/ 오른쪽 6, 7
    # 4 -> 위 2, 5, 6/ 오른쪽 3, 6, 7
    # 5 -> 아래 2, 4, 7/ 오른쪽 3, 6, 7
    # 6 -> 아래 2, 4, 7/ 왼쪽 3, 4, 5
    # 7 -> 위 2, 5, 6/ 왼쪽 3, 4, 5
    # 각자 현재 위치에서 이동 가능한 구조 -> 상하좌우 기준
    possibles = [[],  # 0
                 [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]],  # 1
                 [[1, 2, 5, 6], [1, 2, 4, 7], [], []],  # 2
                 [[], [], [1, 3, 4, 5], [1, 3, 6, 7]],  # 3
                 [[1, 2, 5, 6], [], [], [1, 3, 6, 7]],  # 4
                 [[], [1, 2, 4, 7], [], [1, 3, 6, 7]],  # 5
                 [[], [1, 2, 4, 7], [1, 3, 4, 5], []],  # 6
                 [[1, 2, 5, 6], [], [1, 3, 4, 5], []]]  # 7

    # 큐에는 현재위치, 현재 모양, 남은 시간 을 같이 입력
    queue = deque()
    queue.append((r, c, underground[r][c], L - 1))
    # 방문체크
    underground[r][c] = 9
    # 이동 가능 위치 개수 추가
    ans += 1
    # L -= 1

    # 사방탐색
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    while queue:
        y, x, shape, l = queue.popleft()

        # 일단 시간이 더 남아있지 않으면 진행하지 않음
        if not l:
            continue

        # 상하좌우 탐색하면서,
        # 이동가능하면, 이동시키고,
        # 그렇지 않으면 패스..
        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            # 범위 확인
            if -1 < move_y < N and -1 < move_x < M:
                # 이동해본 위치 move_y, move_x 가 현재 shape에서 이동 가능하다면,
                # 이동 불가능한 경우를 제외시켜 줍니다.

                current = underground[move_y][move_x]

                if current not in possibles[shape][i]:
                    continue

                else:
                    queue.append((move_y, move_x, current, l - 1))
                    underground[move_y][move_x] = 9
                    ans += 1

    return ans


T = int(input())

for tc in range(T):

    N, M, R, C, L = map(int, input().split())

    # 지하 터널 정보
    underground = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc + 1, bfs(R, C, L)))
