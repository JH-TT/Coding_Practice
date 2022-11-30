dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
for i in range(5, 100):
    dp[i] = dp[i-1] + dp[i-5]
for _ in range(int(input())):
    n = int(input())
    print(dp[n-1])

# i번째가 i-1번째값과 i-5번째 값의 합임.