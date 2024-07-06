n = int(input())

dp = [4 for _ in range(n + 1)]
for i in range(1, int(n ** 0.5) + 1):
    dp[i ** 2] = 1

for i in range(2, n+1):
    if dp[i] == 1: continue
    for j in range(int(i ** 0.5), 0, -1):
        if (j ** 2) * 4 < i: break
        dp[i] = min(dp[i], dp[i - j**2] + 1)
print(dp[n])

# dp로 해결한 문제. dp로 안하고도 충분히 단순 완탐으로 풀이 가능하긴함.