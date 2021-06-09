def combi(idx, sidx):

    if sidx == M:
        print(*sel)
        return

    for i in range(idx, N):
        if not check[i]:
            sel[sidx] = arr[i]
            check[i] = True
            combi(i+1, sidx+1)
            check[i] = False


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
sel = [0] * M
check = [False] * N

combi(0, 0)

