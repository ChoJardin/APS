def check_paper(paper):
    global ans

    # 한 가지 숫자로만 채워져 있는가?
    if min(map(min, paper)) == max(map(max, paper)):
        # 맞다면, 개수 더해준다.
        ans[paper[0][0]] += 1
        return

    # 한가지 숫자로만 채워져 있지 않음 -> 9등분
    length = len(paper)
    cut = length // 3
    # 앞에 3등분
    for i in range(0, length, cut):
        sub_paper = paper[i:i+cut]
        # 다시 3등분
        sub_ = []
        for j in range(0, length, cut):
            for k in range(cut):
                sub_.append(sub_paper[k][j:j+cut])
            check_paper(sub_)
            sub_ = []


N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]

# -1/ 0/ 1
ans = {-1: 0, 0: 0, 1: 0}

check_paper(papers)

start = -1
for _ in range(3):
    print(ans[start])
    start += 1
