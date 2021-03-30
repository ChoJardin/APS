def gcd(a, b):  # 최대공약수
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):  # 최소공배수
    return a*b // gcd(a, b)


s = input()
t = input()

a = len(s)
b = len(t)

maximum = lcm(a, b)

max_s = s * (maximum//a)
max_t = t * (maximum//b)

if max_s == max_t:
    print(1)
else:
    print(0)
