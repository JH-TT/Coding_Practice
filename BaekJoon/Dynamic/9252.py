a = [""] + list(input())
b = [""] + list(input())
dp = [[""] * len(a) for _ in range(len(b))]

for i in range(1, len(b)):
    for j in range(1, len(a)):
        if a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1] + b[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
res = dp[-1][-1]
print(len(res), res, sep="\n")

# 이상한점
# print(len(dp[-1][-1]), dp[-1][-1], sep="\n") 은 시간초과가 뜨는건지 의문....