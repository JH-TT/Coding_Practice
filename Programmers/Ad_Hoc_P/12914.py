def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])  % 1234567
    
    return dp[n]

# n칸 멀리뛰기를 하는 경우의 수
# n-1칸까지 가고 1칸뛰기
# n-2칸까지 가고 2칸뛰기
# 이는 코드로 변경하면 dp[n] = dp[n-1] + dp[n-2] 가 된다.