# 중복 순열?
def perm_rep(idx):

    if idx == M:
        print(*sel)
        return

    for i in range(N):
        sel[idx] = arr[i]
        perm_rep(idx+1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sel = [0] * M

perm_rep(0)