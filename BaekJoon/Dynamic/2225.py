# 내가 푼 것.
n, k = map(int, input().split())

cnt = [[0] * 201 for _ in range(201)] # 0으로 채우면 최소 1개는 나옴.
cnt[0] = [0] + [1] * 200
for i in range(1, 201):
    cnt[i][1] = 1

for i in range(1, 201):
    for j in range(1, 201): 
        for h in range(i+1):
            cnt[i][j] += cnt[i - h][j - 1]
            cnt[i][j] %= 1000000000

print(cnt[n][k])


# 다른 사람 코드 참고.(훨씬 빠름)
n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

dp[0][0] = 1

for i in range(n + 1):
    for j in range(1, k + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000 # ***
        
print(dp[n][k]) 

# *** 부분 설명 : n을 k개의 수를 더해서 표현 가능한 경우의 수는
# k개의 수를 더해서 n-1을 나타낸 경우의 수 + k-1개의 수를 더해서 n을 나타낸 경우의 수이다.

# 말 그대로 k개의 수를 더해 n-1을 나타낸 경우의 수의 의미는 그냥 모든 경우에 1만 더해주면 n을 k개의 수를 더한 경우가 되기 떄문.

# 두 번째는 n개를 k-1개로 나타낸 경우마다 0을 더하는 것이아닌 추가해 주면 완성. 