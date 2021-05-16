N, M = map(int, input().split())

not_heard = {}
for _ in range(N):
    not_heard[input()] = 1

both_not = []
for _ in range(M):
    name = input()
    if not_heard.get(name):
        both_not.append(name)

print(len(both_not))
for name in sorted(both_not):
    print(name)