import sys

N, M = map(int, input().split())

pocket_mon = {}
pocket_num = {}
for i in range(1, N+1):
    monster = sys.stdin.readline().strip()
    pocket_mon[monster] = i
    pocket_num[i] = monster

nums = '0123456789'
for _ in range(M):
    quest = input()
    if quest[0] in nums:
        quest = int(quest)
        print(pocket_num[quest])

    else:
        print(pocket_mon[quest])

