def fib(num):
    # 이미 알고 있는 값이다.
    if fibo[num] != (0, 0):
        x, y = fibo[num]
        return x, y

    else:
        x1, y1 = fib(num-1)
        x2, y2 = fib(num-2)
        fibo[num] = ((x1+x2), (y1+y2))
        return fibo[num]


N = int(input())

fibo = [(0, 0)] * 41  # 40보다 작거나 같은 자연수
fibo[0] = (1, 0)
fibo[1] = (0, 1)

for _ in range(N):
    a, b = fib(int(input()))
    print(a, b)
