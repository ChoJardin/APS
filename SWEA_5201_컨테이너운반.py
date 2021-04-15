T = int(input())

for tc in range(T):
    # 컨테이너, 트럭 개수
    container, truck = map(int, input().split())

    containers = list(map(int, input().split()))
    containers.sort(reverse=True)  # 무게가 무거운 순으로 정렬
    # print(containers)

    trucks = list(map(int, input().split()))
    trucks.sort(reverse=True)  # 적재용량이 큰 순으로 정렬
    # print(trucks)

    total_weight = 0

    t = c = 0  # 트럭하고 컨테이너 각각 매치 시작할 번호
    while t < truck and c < container:
        if trucks[t] >= containers[c]:
            total_weight += containers[c]  # 얘네들은 이동하겠습니다.
            # 다음 트럭과 컨테이너를 확인합니다.
            t += 1
            c += 1

        else:  # 컨테이너가 더 무거우면 다음 컨테이너랑 비교가 필요
            c += 1

    print('#{} {}'.format(tc+1, total_weight))