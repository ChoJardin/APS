N, L = map(int, input().split())

num = 0
while N > 0:
    num += 1
    if str(L) not in str(num):
        N -= 1

print(num)
