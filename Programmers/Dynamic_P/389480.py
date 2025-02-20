def solution(info, n, m):
  dp = [[10**6 for _ in range(m)] for _ in range(len(info) + 1)]

  dp[0][0] = 0
  for i in range(1, len(info) + 1):
      a = info[i-1][0]
      b = info[i-1][1]

      for j in range(m):
          dp[i][j] = min(dp[i][j], dp[i-1][j] + a)

          if j + b < m:
              dp[i][j + b] = min(dp[i][j + b], dp[i-1][j])

  return min(dp[-1]) if min(dp[-1]) < n else -1

# dp[x][y]: x개의 보석을 훔쳤을때 B도둑의 흔적이 y개일때 A도둑의 흔적 최소 개수