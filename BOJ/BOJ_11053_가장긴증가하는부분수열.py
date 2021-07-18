N = int(input())
# 수열 입력
arr = list(map(int, input().split()))

# 해당하는 위치가 수열의 가장 마지막 숫자인 경우
# 해당 수열의 개수
dp = [1 for _ in range(N)]

for i in range(1, N):
    # 이전까지 수열의 최댓값
    max_before = 0
    for j in range(i):
        # i 보다 더 작은 숫자이면서, 그때의 수열의 개수가 max_before 보다 작은 경우 갱신
        if arr[j] < arr[i] and max_before < dp[j]:
            max_before = dp[j]
    dp[i] = max_before + 1

print(max(dp))





