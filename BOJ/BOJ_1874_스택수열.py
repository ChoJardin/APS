def find_ans():
    global ans, arr

    stack = []
    find = 0
    for num in range(1, N+1):  # 각 숫자를 확인한다.
        stack.append(num)  # 일단 스택에 추가하기
        ans.append('+')  # 정답에 ans 추가

        if num == arr[find]:  # 찾아야 하는 숫자라면,
            while find < N and stack and arr[find] == stack[-1]:  # 찾아야 하는 숫자가 나오지 않을 때까지
                stack.pop()  # 스택에서 빼주고
                ans.append('-')  # 정답에 pop 추가
                find += 1

    # for문 순회가 종료되었을 때,
    # stack에 남아있음
    while stack:  # stack을 돌면서
        if find < N and stack[-1] != arr[find]:  # 같지 않다 == 수열을 만들지 못함
            ans = 'NO'
            return  # 함수 종료

        # 같다면 계속 팝 추가
        stack.pop()
        ans.append('-')
        find += 1



N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
# print(arr)

ans = []

find_ans()


# for문 순서대로 돌면서
# stack에 넣는다.
# find = 이번에 찾아야 하는 요소의 idx
# 일단 push 하고,
# arr[find] 이게 for문의 숫자와 같다면, pop 진행, -> 그러면서 while로 돌면서 마지막이랑 비교하고
# 만약 다 끝나고 pop을 하는데 arr 이랑 일치하지 않거나 그렇다면,
# NO 출력

if type(ans) == str:  # 스트링타입이라면
    print(ans)
else:  # 찾았음
    for each in ans:
        print(each)
