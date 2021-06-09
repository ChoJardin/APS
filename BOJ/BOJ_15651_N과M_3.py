def perm(idx):

    if idx == M:
        print(*sel)
        return

    for i in range(N):
        sel[idx] = arr[i]
        perm(idx+1)


N, M = map(int, input().split())

arr = [i+1 for i in range(N)]
sel = [0] * M

perm(0)
