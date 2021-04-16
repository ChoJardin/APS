from collections import deque

def move_room(v, room):
    # 지금 실행하는 값 기준 거리를 저장할 리스트
    # distance = [[0] * N for _ in range(N)]

    cnt = 0

    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        y = v[0]
        x = v[1]

        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            # 범위 확인// 이동할 수 있다면 이동//
            if -1 < move_y < N and -1 < move_x < N and arr[y][x] + 1 == arr[move_y][move_x]:
                queue.append((move_y, move_x))
                cnt += 1

    # # 이번 반복에서 최댓값 확인..
    # max_now = -1
    # for each in distance:
    #     # print(each)
    #     if max(each) > max_now:
    #         max_now = max(each)

    # 저장된 값이랑 이번 반복 결과 비교..
    if cnt > max_value[1]:  # max_value == [room, cnt]
        max_value[1] = cnt
        max_value[0] = room

    elif cnt == max_value[1] and max_value[0] > room:
        max_value[0] = room


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = [99999999, 0]

    # 각 방마다?
    # 사방탐색 해보는 겁니다..
    for i in range(N):
        for j in range(N):
            move_room((i, j), arr[i][j])  # 기준점, room

    print('#{} {} {}'.format(tc+1, max_value[0], max_value[1]+1))