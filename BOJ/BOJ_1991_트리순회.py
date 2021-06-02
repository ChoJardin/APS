import sys
input = sys.stdin.readline


# 전위
def pre_order(v):

    print(chr(v+65), end='')

    # 왼쪽 자식이 있다면,
    if l_child[v] != '.':
        pre_order(ord(l_child[v])-65)

    # 오른쪽 자식이 있다면
    if r_child[v] != '.':
        pre_order(ord(r_child[v])-65)


# 중위
def in_order(v):
    # 왼쪽 자식이 있다면,
    if l_child[v] != '.':
        in_order(ord(l_child[v])-65)

    print(chr(v+65), end='')

    # 오른쪽 자식이 있다면
    if r_child[v] != '.':
        in_order(ord(r_child[v])-65)


# 후위
def post_order(v):
    # 왼쪽 자식이 있다면,
    if l_child[v] != '.':
        post_order(ord(l_child[v])-65)

    # 오른쪽 자식이 있다면
    if r_child[v] != '.':
        post_order(ord(r_child[v])-65)

    print(chr(v+65), end='')


N = int(input())

# 아스키 코드 기준으로 저장
# ord('A') == 65
l_child = ['.'] * N
r_child = ['.'] * N

for _ in range(N):
    p, l, r = input().split()
    # 자식이 있다면 등록
    if l != '.':
        l_child[ord(p)-65] = l

    if r != '.':
        r_child[ord(p)-65] = r

# 항상 'A'가 루트 노드
pre_order(0)
print()
in_order(0)
print()
post_order(0)

