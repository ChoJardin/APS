def perm_rep(idx):

    if idx == M:
        print(*sel)
        return

    for i in range(len(arr)):
        sel[idx] = arr[i]
        perm_rep(idx+1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))
sel = [0] * M

perm_rep(0)
