s1 = input()
s1 = '_' + s1
s2 = input()
s2 = '_' + s2

dp = [[0] * (len(s1)) for _ in range(len(s2))]

for i in range(1, len(s2)):
    for j in range(1, len(s1)):

        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        if s1[j] == s2[i]:
            dp[i][j] = dp[i-1][j-1] + 1

print(max(map(max, dp)))
