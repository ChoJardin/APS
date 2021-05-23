## input() 을 사용하면 시간초과가 나옵니다!

import sys

M = int(input())

arr = [False] * 21  # 들어있으면 true, 없으면 false
for _ in range(M):
    compute = sys.stdin.readline().strip()
    if compute == 'all':
        arr = [True] * 21
    elif compute == 'empty':
        arr = [False] * 21
    else:
        rule, num = compute.split()
        num = int(num)

        if rule == 'add' and not arr[num]:
            arr[num] = True

        elif rule == 'remove' and arr[num]:
            arr[num] = False

        elif rule == 'check':
            if arr[num]:
                print(1)
            else:
                print(0)

        elif rule == 'toggle':
            if arr[num]:
                arr[num] = False
            else:
                arr[num] = True




