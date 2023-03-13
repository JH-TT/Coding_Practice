f = input()
s = input()
t = input()

dp = [[[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)] for _ in range(len(f)+1)]

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        for h in range(1, len(dp[0][0])):
            if f[i-1] == s[j-1] and s[j-1] == t[h-1]:
                dp[i][j][h] = dp[i-1][j-1][h-1] + 1
            else:
                dp[i][j][h] = max(dp[i-1][j][h], dp[i][j-1][h], dp[i][j][h-1])
print(dp[-1][-1][-1])

# LCS 응용문제
# 2개를 비교한 방식에 1차원이 더해진 정도
# 로직은 2개를 비교할때와 같음