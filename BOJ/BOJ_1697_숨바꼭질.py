from collections import deque


def move(s, i):
    if i == 0:
        return s-1
    elif i == 1:
        return s+1
    else:
        return 2*s


def find(s, b, cnt):  # 수빈/ 동생/ cnt

    queue = deque()
    queue.append((s, cnt))
    visited[s] = True

    while queue:
        (s, cnt) = queue.popleft()

        if s == b:  # 수빈이가 동생 찾았다.
            # 큐라서 찾으면 무조건 최소
            return cnt

        for i in range(3):
            next = move(s, i)  # 다음으로 이동하는 장소
            if 0 <= next <= 100000 and not visited[next]:  # 범위 안에 들어오고, 방문한 적이 없다면,
                queue.append((next, cnt+1))  # 큐에 올려주고
                visited[next] = True  # 방문쳌


S, B = map(int, input().split())

visited = [False for _ in range(0, 100002)]

ans = find(S, B, 0)

print(ans)


