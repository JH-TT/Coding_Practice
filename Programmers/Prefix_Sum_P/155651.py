def solution(book_time):
    answer = 0
    n = 24 * 60 + 10
    dp = [0] * n
    
    for t in book_time:
        start, end = t
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        dp[s_h*60 + s_m] += 1
        dp[e_h*60 + e_m + 10] -= 1
    for i in range(n-1):
        dp[i+1] += dp[i]
    
    return max(dp)

# start부분은 +1, end부분은 -1로 두어서 나중에 한번에 누적합을 구한다.
# 그 중에 최댓값을 리턴