def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    INF = float('inf')
    for i in problems:
        max_alp = max(max_alp, i[0])
        max_cop = max(max_cop, i[1])
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i+1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j+1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
                
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp, next_cop = min(max_alp,i + alp_rwd), min(max_cop,j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
    
    return dp[-1][-1]

# dp문제일 줄 몰랐다... 단순 백트래킹 이용하니 시간초과 떴음. 개수도 100개까지길래 부르트포스 이용했더니 바로 시간초과