# N개의 피자 굽기
# M개의 피자 순서대로 화덕에 넣고 치즈가 녹으면 화덕에서 꺼내기
# 남아있는 피자의 번호를 알아내는 프로그램

# 피자를 구워보자
# 주의해야 할 것;
# 1.더이상 대기하고 있는 피자가 없을 때  2.화덕 크기 N  3.화덕에 피자가 1개 남았을 때 그만하면 됨
def pizza_in_the_fire():
    # print('start')
    # 화덕
    foyer = []

    # N개의 피자를 화덕에 넣어본다.
    for _ in range(N):
        foyer.append(queue.pop(0))

    # 이제 치즈를 확인해야 할 차례
    # 그냥 안에서 break 해주고 무한 반복합시다..
    # check 를 모듈연산해준 아이를 확인해도 되나요..?
    # 그럼 나중에 피자 없어지면 index 에러 확인 잘 해야 함..
    check = 0
    cnt = 0  # 비어있는 화덕 개수
    while True:
        # 인덱스에러 나지 말아랏
        check %= N

        # 화덕에 1개만 들어있음
        if cnt == N -1:
            # True인 피자를 확인
            for i in range(N):
                if foyer[i]:
                    return foyer[i][0]

        # check번째 피자의 치즈 확인
        # 빈 화덕이 아니라면
        if foyer[check]:
            foyer[check][1] //= 2

            # 치즈 다 녹음
            if not foyer[check][1]:
                # 피자 빼고
                foyer.pop(check)

                # 대기 피자 있으면 그 자리에 추가
                if queue:
                    foyer.insert(check, queue.pop(0))
                # 대기 피자 없으면 빈리스트 넣어주까...
                else:
                    foyer.insert(check, [])
                    cnt += 1

        check += 1


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())  # N == 화덕 크기, M == 피자 개수

    # 피자대기줄
    queue = []
    pizza = list(map(int, input().split()))

    for idx, cheese in enumerate(pizza):
        queue.append([idx+1, cheese])
    # print(queue)

    print('#{} {}'.format(tc+1, pizza_in_the_fire()))
