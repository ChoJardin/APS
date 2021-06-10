def sequence(idx, sidx):

    if sidx == M:
        print(*sel)
        return

    for i in range(idx, len(arr)):
        if cnt[arr[i]]:
            sel[sidx] = arr[i]
            cnt[arr[i]] -= 1
            sequence(i, sidx+1)
            cnt[arr[i]] += 1


N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 숫자가 몇개 들어있나..
cnt = {}
for each in arr:
    cnt[each] = cnt.get(each, 0) + 1
# 중복 제거 후 정렬
arr = sorted(list(set(arr)))
sel = [0] * M

sequence(0, 0)