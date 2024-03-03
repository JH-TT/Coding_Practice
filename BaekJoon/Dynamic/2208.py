import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewel = [int(input()) for _ in range(n)]
pre_jewel = [0]

for i in range(len(jewel)):
    pre_jewel.append(pre_jewel[-1] + jewel[i])

min_value = 10**8
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i >= m:
        min_value = min(min_value, pre_jewel[i - m]) # i-m번째까지 중에 최솟값을 업데이트 한다.
        dp[i] = max(dp[i-1], pre_jewel[i] - min_value) # 지금까지 최댓값이랑 i번째 누적합 - 최솟값과 비교해서 업데이트 한다.
    else:
        dp[i] = dp[i-1]
print(dp[n])