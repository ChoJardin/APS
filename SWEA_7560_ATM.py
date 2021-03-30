T = int(input())

for tc in range(T):
    N = int(input())
    time = list(map(int, input().split()))

    time.sort(reverse=True)

    sum = 0
    for i, v in enumerate(time):
        sum += v * (i+1)

    print('#{} {}'.format(tc+1, sum))