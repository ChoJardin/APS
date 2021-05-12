def add_num(y, x, now_num):
    # print(y, x, now_num)
    if len(now_num) == 7:  # 7자리가 완성되었습니다.
        results.add(now_num)
        return

    # 아직 완성되지 않았으면, 추가시킵니다.
    # 사방탐색해가면서 만들어주고..
    for i in range(4):
        move_y = y + dy[i]
        move_x = x + dx[i]

        # 범위확인
        if -1 < move_y < 4 and -1 < move_x < 4:
            # 범위 들어오면 그냥 이동..
            add_num(move_y, move_x, now_num+arr[move_y][move_x])


T = int(input())

for tc in range(T):
    arr = [input().split() for _ in range(4)]  # 4*4배열
    # print(arr)

    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]

    # 결과들을 저장해보겠음
    results = set()
    # 각 값에 고유값을 붙여서 관리함 -> 탐색 시간이 O(1)
    # 리스트로 하면 탐색시간이 길이만큼 걸리게 된다..

    # 각 점을 기준으로 add_num 함수 실행
    # 완전탐색으로 생각됩니다..
    for i in range(4):
        for j in range(4):
            add_num(i, j, arr[i][j])  # y, x, now_num

    print('#{} {}'.format(tc+1, len(results)))
