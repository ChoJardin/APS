# 중복조합
def combi_rep(idx, sidx):

    if sidx == M:
        print(*sel)
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combi_rep(i, sidx+1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sel = [0] * M

combi_rep(0, 0)

