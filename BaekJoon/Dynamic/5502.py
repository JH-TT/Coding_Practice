n = int(input())
pal = input()
lap = pal[::-1]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if pal[i-1] != lap[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = dp[i-1][j-1] + 1
print(n-dp[-1][-1])

# 주어진 문자열과 반대로 뒤집은 문자열을 만들고
# LCS를 실행한다.
# 그러면 그 LCS의 값은 현재 가장 팰린드롬의 길이가 되고 그 값을 n에서 뺀다.