T = int(input())

for tc in range(T):
    # 힙은 완전이진? 무조건 왼쪽 자식부터 가진다.
    # 들어오는 값이 크다면, 자식으로 만들고,
    # 작다면, 부모로 만들고
    N = int(input())
    value = list(map(int, input().split()))

    # 자연수가 주어진다.
    heap = [0] * (N+1)

    # 값을 받아서 채워보자
    for i in range(N):
        if not i:  # 처음 들어오는 입력값이면
            heap[1]= value[i]
            last = 1

        else:
            # 무언가 값이 있으면
            # 그 다음에 값을 추가해야겠지
            last += 1
            heap[last] = value[i]

            # 이제 값은 더했으니까 부모노드랑 비교해서 작은지 큰지 확인이 필요
            # 부모가 더 큰 경우에는 가보자
            check = last
            while heap[check] < heap[check//2]:
                heap[check], heap[check//2] = heap[check//2], heap[check]
                check = check//2

    # print(heap)  # heap 된 것 같습니당..

    plus = N//2  # 더할 노드들..
    sum = 0
    while plus > 0:
        sum += heap[plus]
        plus = plus//2

    print('#{} {}'.format(tc+1, sum))
