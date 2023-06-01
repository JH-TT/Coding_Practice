def solution(n):
    dp = [0] * 100001
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10
    mod = 1000000007
    for i in range(4, n+1):
        dp[i] = (dp[i-1] + dp[i-2] * 2 + dp[i-3] * 6 + dp[i-4] - dp[i-6] + mod) % mod
    
    return dp[n]

# https://velog.io/@song961003/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EB%B0%A9%EA%B0%80%EB%A5%B4%EB%93%9C-%ED%83%80%EC%9D%BC-JS
# 상당히 점화식을 깔기 까다로운 문제였음...