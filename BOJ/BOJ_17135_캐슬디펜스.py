from itertools import combinations
from collections import deque
import copy


def bfs(v, plan):
    global N, M, D

    # 좌, 상, 우
    # 같은 거리에 있는 경우 왼쪽의 적부터 공격한다.
    # 같은 거리인 경우, queue에서 먼저 나오는 애가 왼쪽
    dy = [0, -1, 0]
    dx = [-1, 0, +1]

    # 거리정보 저장
    distance = [[0] * M for _ in range(N)]

    queue = deque()
    queue.append((v, 1))  # 좌표값, 현재 거리

    while queue:
        (y, x), d = queue.popleft()
        if plan[y][x]:  # 적이 있다면,
            return (y, x)  # 이 적을 공격하겠다.

        # 아직 적을 만나지 못했다.
        for i in range(3):
            moved_y = y + dy[i]
            moved_x = x + dx[i]

            # 범위 확인, 궁수가 공격 가능한 범위 안에 있는가?, 아직 방문하지 않았나
            if -1 < moved_y < N and -1 < moved_x < M and d+1 <= D and not distance[moved_y][moved_x]:
                # 거리 등록
                distance[moved_y][moved_x] = d+1
                # 큐에 올리기
                queue.append(((moved_y, moved_x), d+1))


def attack(castle):
    killed = 0  # 해치운 적

    # 각 성의 자리에서부터 거리 확인해서 가장 가까운 적이 D 안에 있는가? -> 그 적을 선택
    # 공격은 한번에
    # 공격이 끝나면 1을 전부 하나씩 내리고,
    # 남은 적이 없다면, killed를 반환한다.

    plan = copy.deepcopy(enemy)

    # 적이 남아있는 경우 반복
    while max(map(max, plan)):
        attack_point = set()  # 같은 적을 한번에 공격할 수도 있다.

        # 각 성의 위치에서
        for i in range(3):
            archer = castle[i]
            target = bfs((N-1, archer), plan)
            if target:
                attack_point.add(target)  # 공격할 적의 위치 반환

        # 공격할 대상이 있는 경우,
        if attack_point:
            # 공격은 한번에 일어난다.
            for each in attack_point:
                plan[each[0]][each[1]] = 0  # 공격했다
                killed += 1  # 해치웠음

        # 적이 한칸씩 이동해서 내려온다.
        plan = [[0] * M] + plan[:-1]

    return killed


N, M, D = map(int, input().split())  # 행, 열, 공격 가능 거리
enemy = [list(map(int, input().split())) for _ in range(N)]

castles = list(combinations([i for i in range(M)], 3))  # 궁수가 위치할 성

ans = []
for castle in castles:
    ans.append(attack(castle))

print(max(ans))
