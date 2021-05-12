def winner():
    a = []  # 1
    b = []  # 2
    cnt = 0
    while cards:
        # 순서대로 카드 하나씩 가져가기
        if cnt % 2:  # 홀수
            b.append(cards.pop(0))
            for i in range(len(b)):
                if b.count(b[i]) >= 3:
                    return 2
                if b[i] + 1 in b and b[i] + 2 in b:
                    return 2

        else:  # 짝수
            a.append(cards.pop(0))
            for i in range(len(a)):
                if a.count(a[i]) >= 3:
                    return 1
                if a[i] + 1 in a and a[i] + 2 in a:
                    return 1
        cnt += 1

    return 0



T = int(input())

for tc in range(T):
    cards = list(map(int, input().split()))

    # 연속인 숫자가 3개 이상이면 run
    # 같은 숫자가 3개 이상이면 triplet

    print('#{} {}'.format(tc+1, winner()))

