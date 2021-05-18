N, M = map(int, input().split())

if M > N//2:
    M = N - M

up = 1
for i in range(N, N-M, -1):
    up = up * i

down = 1
for i in range(M, 0, -1):
    down = down * i

print(up//down)


