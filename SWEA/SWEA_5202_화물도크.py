
T = int(input())

for tc in range(T):
    N = int(input())

    # 시작시간, 종료시간
    time = [0] * 25  # 23? 24?
    '''
    1. 가장 빨리 끝나는 시간대 
    2. 가장 가까운 게 그 다음 작업할 것 
    '''
    applications = [list(map(int, input().split())) for _ in range(N)]
    # 끝나는 시간을 기준으로 정렬해야 합니다..
    for idx, each in enumerate(applications):
        applications[idx] = [each[1], each[0]]
    # 끝나는 시간이 빠른 역순으로 정렬
    applications.sort(reverse=True)
    # print(applications)

    cnt = 0
    while applications:
        application = applications.pop()

        # 맨 처음이라면, 픽
        if not cnt:
            now = application
            cnt += 1

        # 맨 처음이 아니라면
        else:
            # 지금 시간 다음에 시작하는 애면 고르기
            # 빨리 끝나는 순으로 가져오게 됩니다..
            if application[1] >= now[0]:  # 지금의 끝나는 시간하고, 나중에 오는 애 시작하는 시간하고 비교
                now = application
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))
