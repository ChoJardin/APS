N = int(input())
meetings = []
for _ in range(N):
    meetings.append(tuple(map(int, input().split())))
# print(meetings)

# 먼저 끝나는 순으로 정렬 -> 같은 시간에 끝나면, 먼저 시작하는 회의가 먼저 온다
meetings.sort(key=lambda x: (x[1], x[0]))
# print(meetings)

cnt = 1
meeting_opened = meetings[0]
for i in range(1, N):
    if meetings[i][0] >= meeting_opened[1]:  # 지금 열리고 있는 회의 끝나고 시작한다면,
        meeting_opened = meetings[i]  # 지금 열리는 회의 바꿔주고,
        cnt += 1  # 회의 개수 증가

print(cnt)
