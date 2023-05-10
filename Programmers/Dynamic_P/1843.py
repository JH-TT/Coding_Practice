import sys

def solution(arr):
    answer = -1
    expr = [a for a in arr if a in ["-", "+"]]
    dp = [int(a) for a in arr if a not in ["-", "+"]]
    n = len(dp)
    
    INF = sys.maxsize
    MIN_DP = [[INF for _ in range(n)] for _ in range(n)]
    MAX_DP = [[-INF for _ in range(n)] for _ in range(n)]
    
    for i in range(n): # 자기 자신으로 초기화
        MIN_DP[i][i] = dp[i]
        MAX_DP[i][i] = dp[i]
    
    for step in range(1, n): # i부터 j까지 떨어진 거리
        for i in range(n):
            j = i + step
            if j >= n:
                continue

            # 최솟값도 구하는 이유?(이 문제의 핵심)
            # 더하기는 그냥 최댓값끼리 계산하면 되지만, 뺄셈은 최댓값에서 최솟값을 뺀 것이 최댓값이 되기 때문에 최솟값에 대한 정보도 필요하다. 
            for k in range(i+1, j+1): # 하나씩 확인
                if expr[k-1] == "+": # 더하기는 최댓값은 (최댓값 + 최댓값) 최솟값은 (최솟값 + 최솟값)
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k-1] + MAX_DP[k][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k-1] + MIN_DP[k][j])
                else: # 빼기는 최댓값 : (최댓값 - 최솟값), 최솟값 : (최솟값 - 최댓값)
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k-1] - MIN_DP[k][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k-1] - MAX_DP[k][j])

    return MAX_DP[0][n-1]

# 설명이 길어서 참고해야 한다
# https://school.programmers.co.kr/questions/35224
# https://www.ai-bio.info/programmers/1843