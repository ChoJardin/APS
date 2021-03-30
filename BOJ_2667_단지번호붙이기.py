N = int(input())

# N * N 입력
arr =[list(map(int, list(input()))) for _ in range(N)]
# visited = [[False] * N for _ in range(N)]
stack = []
houses = []

# DFS
# delta 이동하면서 visited = True해주고
# cnt 를 올리고

# 상하좌우
dy = [-1, +1, 0, 0]
dx = [0, 0, -1, +1]

for i in range(N):
    for j in range(N):
        # 집이고 방문 안 했으면
        cnt = 0
        # 1이다
        if arr[i][j]:  # and not visited[i][j]:
            stack.append((i, j))
            # visited[i][j] = True
            # 이동 못하게 막아준다.
            arr[i][j] = 0

            while stack:
                v = stack.pop()
                # 방문쳌
                # visited[v[0]][v[1]] = True
                # 집 몇채인가 확인해준다.
                cnt += 1

                # 이동하면서 근처의 집을 확인해본다.
                for idx in range(4):
                    y = v[0] + dy[idx]
                    x = v[1] + dx[idx]
                    # 집이고 방문 안 했으믄 추가해준다.
                    if -1 < x < N and -1 < y < N and arr[y][x]:  # and not visited[y][x]:
                        stack.append((y, x))
                        # 여기서 방문쳌을 해줘야 중복으로 세지 않음
                        # visited[y][x] = True
                        arr[y][x] = 0

            # 단지 확인이 끝났음
            houses.append(cnt)

houses.sort()
print(len(houses))
for house in houses:
    print(house)