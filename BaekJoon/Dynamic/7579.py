n, m = map(int, input().split())
active = list(map(int, input().split())) # 활성화상태 메모리
inactive = list(map(int, input().split())) # 비활성화 시킬때 사용되는 비용

dp = [[0 for _ in range(sum(inactive)+1)] for _ in range(n+1)]
res = sum(inactive) # 최댓값

# 이전값을 이어서 가는것이기 때문에 1부터 시작.
for i in range(1, n+1):
    byte = active[i-1] # 해당 앱 메모리
    cost = inactive[i-1] # 해당 앱 비활성화 비용
    for j in range(1, sum(inactive)+1):
        if j < cost: # cost보다 적으면 비활성화를 못시킴.(이전값 그대로)
            dp[i][j] = dp[i-1][j]
        else: # 비활성화가 가능하다면 이전값이랑 비교
            # max(지금까지 늘린 메모리, 현재 앱을 비활성화 시켜서 늘린 총 메모리)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte)
        # m을 넘겼다는 것은 조건을 만족시켰다는 의미. res를 업데이트 시켜준다.
        if dp[i][j] >= m:
            res = min(res, j)
print(res)

# dp에 냅색문제인것은 알았지만, 어떤식으로 활용할지가 애매했음.
# 계속 m에만 집중하다보니 삽질만 한듯. 범위가 적은것을 기준으로!