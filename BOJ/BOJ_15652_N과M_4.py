# 중복 조합
def combination_rep(idx, sidx):

    if sidx == M:
        print(*sel)
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination_rep(i, sidx+1)


N, M = map(int, input().split())

arr = [i+1 for i in range(N)]
sel = [0] * M

combination_rep(0, 0)