import sys
sys.setrecursionlimit(100000)


def clean(r, c, d, check):  # r, c, direction, 4방향 확인 여부
    global cnt

    # print(r, c, d, check)

    # 사방탐색
    # 북, 동, 남, 서 == 상, 우, 하, 좌
    dy = [-1, 0, +1, 0]
    dx = [0, +1, 0, -1]

    # 4방향 모두 청소되어 있거나 벽인 경우,  # 회전만 했음
    if check == 4:
        # 바라보는 방향을 유지하면서 1번 후진하고 왼쪽 탐색을 계속..
        change_d = (d+2) % 4
        y = r + dy[change_d]
        x = c + dx[change_d]

        # 뒤쪽이 벽이면 후진도 못하지
        if arr[y][x] != 1:  # 벽이 아니면 후진은 해보자
            clean(y, x, d, 0)
            return
        else:
            return

    else:
        # 1. 현재 위치를 청소한다.
        # 방이고, 청소할 수 있다면,
        if arr[r][c] == 0 and not visited[r][c]:
            cnt += 1  # 청소했다
            visited[r][c] = True  # 다시 청소 방지

        # 방향 바꾸기
        change_d = d - 1
        if change_d == -1:
            change_d = 3

        # 확인해 봐야 할 왼쪽 방향..
        y = r + dy[change_d]
        x = c + dx[change_d]

        # 왼쪽에 아직 청소하지 않은 공간이 있다면,
        if arr[y][x] == 0 and not visited[y][x]:
            clean(y, x, change_d, 0)  # 청소해준다
            return
        # 공간이 있는데 청소를 했거나, 벽이라면
        if (arr[y][x] == 0 and visited[y][x]) or arr[y][x] == 1:
            clean(r, c, change_d, check+1)  # 회전만 합니다.
            return


N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# print(arr)

cnt = 0

clean(r, c, d, 0)

print(cnt)