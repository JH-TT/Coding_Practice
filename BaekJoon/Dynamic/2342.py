dist = [[1, 2, 2, 2, 2],
  [2, 1, 3, 4, 3],
  [2, 3, 1, 3, 4],
  [2, 4, 3, 1, 3],
  [2, 3, 4, 3, 1]]

seq = list(map(int, input().split()))[:-1]

INF = float('inf')
dp = [[INF for _ in range(5)] for _ in range(5)]
dp[0][0] = 0

for s in seq:
new_dp = [[INF for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        cur = dp[i][j]
        if cur == INF:
            continue

        # 왼발로 누르기
        c1 = cur + dist[i][s]
        if new_dp[s][j] > c1:
            new_dp[s][j] = c1

        c2 = cur + dist[j][s]
        if new_dp[i][s] > c2:
            new_dp[i][s] = c2

dp = new_dp

ans = min(min(row) for row in dp)
print(ans)

# 아무리 많아야 경우의 수가 25개뿐이라 dp를 계속 만들어서 업데이트 해주는 방식으로 한다.
# dp에 INF가 아니면 바로 최솟값을 구해서 넣는 방식으로 한다.