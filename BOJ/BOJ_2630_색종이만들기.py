def make_paper(ys, ye, xs, xe):  # y 시작, y끝, x시작, x끝
    global white, blue

    # 이번 재귀에서 확인해야 하는 종이
    need_check = []
    for line in paper[ys:ye+1]:
        need_check.append(line[xs:xe+1])

    # 한가지 색만 있다면,
    if max(map(max, need_check)) == 0:  # 흰색
        white += 1
        return
    if min(map(min, need_check)) == 1:  # 파란색
        blue += 1
        return

    # 여러색이 섞여있음 -> 4등분해서 확인 필요
    mid_y = (ys+ye) // 2
    mid_x = (xs+xe) // 2

    # 1사분면
    make_paper(ys, mid_y, mid_x+1, xe)
    # 2사분면
    make_paper(ys, mid_y, xs, mid_x)
    # 3사분면
    make_paper(mid_y+1, ye, xs, mid_x)
    # 4사분면
    make_paper(mid_y+1, ye, mid_x+1, xe)


N = int(input())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0

make_paper(0, N-1, 0, N-1)

print(white)
print(blue)