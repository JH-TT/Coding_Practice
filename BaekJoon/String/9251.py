s1 = "-" + input()
s2 = "-" + input()

dp = [[0] * len(s2) for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 부분수열은 연속된 값이 아니다.
            # 따라서 현재의 문자를 비교하는 과정 이전의 최대 공통부분수열은 계속해서 유지되는데
            # 이때 이전의 과정이 dp[i-1][j]와 dp[i][j-1]이다.
print(dp[-1][-1]) 

# 참고 : https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
