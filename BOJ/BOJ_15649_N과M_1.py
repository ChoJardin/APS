def perm(idx):

    if idx == M:
        print(*sel)
        return

    for i in range(N):
        # 아직 사용하지 않았으면,
        if not check[i]:
            check[i] = True  # 사용 확인
            sel[idx] = arr[i]  # 사용 해주고
            perm(idx+1)
            check[i] = False


N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
check = [False] * N  # 사용 확인
sel = [0] * M  # 이게 완성된 수열

perm(0)