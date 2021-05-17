import sys
input = sys.stdin.readline


def make_combi():
    global cnt, ans

    if cnt == M:  # 원하는 개수를 다 골랐다
        print(*ans)  # 출력
        return

    for i in range(N):
        if not check[i]:  # 사용된 숫자가 아니다

            ans.append(nums[i])  # i번째 숫자를 사용하겠음
            check[i] = True  # 사용 확인 해주고
            cnt += 1  # 1개 골랐다고 표시하고

            make_combi()  # 다음 숫자 찾으

            # 찍고 돌아왔으니까 초기화
            check[i] = False
            cnt -= 1
            ans = ans[:-1]


N, M = map(int, input().strip().split())

nums = list(map(int, input().strip().split()))
nums.sort()

ans = []
check = [False for _ in range(1, N+1)]  # 사용되었는가?
cnt = 0  # 몇개의 숫자를 골랐나?

make_combi()