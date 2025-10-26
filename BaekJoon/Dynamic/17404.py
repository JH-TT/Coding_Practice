n = int(input())

INF = int(1e9)
rgb = [list(map(int, input().split())) for _ in range(n)]
res = INF

for start in range(3):
    dp = [[INF] * 3 for _ in range(n)]

    dp[0][start] = rgb[0][start]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

    for end in range(3):
        if start == end:
            continue
        res = min(res, dp[n-1][end])

print(res)

# 첫번째 집이 R인 경우 최솟값
# 첫번째 집이 G인 경우 최솟값
# 첫번째 집이 B인 경우 최솟값
# R, G, B중에 최솟값
# 이 순서로 구해야한다.
# 따라서 이 문제는 각각 DP로 최솟값을 구한뒤에 최종 최솟값을 구하는 방식이다.
# DP를 3번 돌린다 보면된다.
# 마지막 집은 1번집과 색이 달라야 하기때문에 코드에서 마지막부분에 첫번째와 색이 다른 비용만 최솟값 계산에 넣었다.