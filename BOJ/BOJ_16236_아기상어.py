from collections import deque


def eat_fish():
    global shark, ate, time_passed, is_left

    fish_list = []
    now = ()

    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:  # 상어라면,
                now = (i, j)  # 현재 상어 위치 저장
                fish_list = bfs(i, j, 0)  # 탐색 시작
                break

    if fish_list:  # 먹을 수 있는 물고기가 있다면,
        min_dist = 9999999
        min_location = []
        for fish in fish_list:  # 먹을 수 있는 물고기 중에서
            if fish[2] < min_dist:  # 제일 가까이 있는 물고기라면,
                min_location = (fish[0], fish[1])
                min_dist = fish[2]

            elif fish[2] == min_dist:  # 같은 거리에 있다
                # 맨 위, 맨 왼쪽
                if min_location[0] > fish[0]:  # 이번 물고기가 더 위에 있다면,
                    min_location = (fish[0], fish[1])
                elif min_location[0] == fish[0] and min_location[1] > fish[1]:  # 더 왼쪽에 있는 애 선택
                    min_location = (fish[0], fish[1])

        ate += 1  # 물고기를 먹는다
        time_passed += min_dist  # 시간 경과
        sea[min_location[0]][min_location[1]] = 9  # 상어 이동
        sea[now[0]][now[1]] = 0

        if ate == shark:  # 먹은 물고기의 수가 상어의 수와 같아지면,
            shark += 1  # 상어 크기 1 증가
            ate = 0  # 먹은 물고기 수 초기화
    else:
        is_left = False

    return


def bfs(y, x, d):
    global shark

    distance = [[0] * N for _ in range(N)]  # 방문체크/ 거리 등록
    eatable = []  # 먹을 수 있는 물고기 정보

    # 델타 탐색
    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    queue = deque()
    queue.append((y, x, d))

    while queue:
        y, x, d = queue.popleft()  # y값, x값, 상어로부터의 거리

        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]

            # 범위 확인, 방문 확인, 이동가능여부==상어보다 크지 않은 물고기인지 확인, 상어의 위치인지 확인
            if -1 < move_y < N and -1 < move_x < N and not distance[move_y][move_x] and sea[move_y][move_x] <= shark and (move_y, move_x) != (y, x):

                fish = sea[move_y][move_x]  # 이동하는 칸에 있는 물고기

                if not fish:  # 물고기가 없다면
                    distance[move_y][move_x] = d + 1  # 거리 정보 갱신
                    queue.append((move_y, move_x, d+1))  # 이동

                elif fish == shark or fish == 9:  # 물고기의 크기가 상어와 같다면, 이동만 가능
                    distance[move_y][move_x] = d + 1  # 방문 확인
                    queue.append((move_y, move_x, d+1))  # 이동

                else:  # 물고기가 상어보다 작다 == 이동하고 먹을 수 있음
                    distance[move_y][move_x] = d + 1  # 방문 체크
                    eatable.append((move_y, move_x, d+1))  # 먹을 수 있다
                    queue.append((move_y, move_x, d+1))  # 이동

    return eatable  # 먹을 수 있는 물고기 return


def find_min():  # 제일 작은 물고기 찾기
    min_value = 99999999
    for i in range(N):
        for j in range(N):
            # 바다가 아니면서 가장 작은 값 == 가장 작은 물고기
            if sea[i][j] and min_value > sea[i][j]:
                min_value = sea[i][j]
    return min_value


N = int(input())

sea = [list(map(int, input().split())) for _ in range(N)]

# 9 == 아기상어의 위치
# 9 가 있는 지점에서 bfs 탐색 시작..
# 0 이 아닌 숫자가 있고, == 물고기가 있음
# 아기상어의 크기보다 작다면 == 먹기 위에 queue에 넣는다.  -> eatable 리스트를 만들겠다.  거리와 함께 추가하겠음
# 아기상어의 크기와 같다면 == 이동은 할 수 있다.
# for 문 반복이 끝났을 때마다 == 거리가 같은 애들만 Eatable에 들어있음
# -> eatable을 확인하면서 if len(eatable) == 1: 그 고기를 먹고,
# eatable 이 1보다 크다면, 더 위에, 그 중에서 왼쪽에 있는 순서대로 먹고 다시 bfs 새로 탐색 시작

shark = 2  # 상어 크기
ate = 0  # 먹은 물고기
time_passed = 0  # 몇 초 경과
is_left = True  # 먹을 수 있는 물고기 남아있음

# sea에 상어가 잡아먹을 수 있는 물고기가 남아있는 동안 계속 진행..
while find_min() < shark and is_left:
    eat_fish()

print(time_passed)





