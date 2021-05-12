from itertools import permutations

def perm(idx):

    if idx == N-1:
        pick.append(sel[:])
        return

    else:
        for i in range(N-1):
            if check[i] == 0:
                sel[idx] = visit[i] #값을 써라
                check[i] = 1 #사용을 했다는 표시
                perm(idx+1)
                check[i] = 0 #다음 반복문을 위한 원상복구


T = int(input())

for tc in range(T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    N = len(arr)

    visit = [i for i in range(1, N)]  # 지나갈 장소
    sel = [0] * (N-1)  # 결과들이 저장될 리스트
    check = [0] * (N-1)  # 해당 원소를 이미 사용했는지 안했는지에 대한 체크
    pick = []

    # pick = list(permutations(visit, N-1))
    perm(0)
    # print(pick)

    min_distance = 9999999999
    for each in pick:
        # 각 순열의 길이는 N-1
        now_distance = 0
        for i in range(N-1):
            if i == 0:
                now_distance += arr[0][each[i]]
            else:
                now_distance += arr[each[i-1]][each[i]]

        # 돌아가기
        now_distance += arr[each[i]][0]

        if min_distance > now_distance:
            min_distance = now_distance

    print('#{} {}'.format(tc+1, min_distance))
