def solution(s):
    answer = 1
    
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
    
    for i in range(len(s) + 1):
        dp[i][i] = 1

    for w in range(1, len(s)):
        for i in range(1, 1 + len(s)-w):
            if s[i-1] != s[i+w-1]:
                continue
            if w == 1: # 길이가 2면 양쪽이 같은지만 보면 됨
                dp[i][i+w] = 1
                answer = w+1
                continue
            if dp[i+1][i+w-1]:
                dp[i][i+w] = 1
                answer = w+1

    return answer

# 비슷한 문제들을 풀어봤기에 같은 방식으로 해결