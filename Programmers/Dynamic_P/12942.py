def solution(ms):
    answer = 0
    n = len(ms)
    INF = float('inf')
    # dp[i][j] -> i번째 행렬부터 j번째 행렬의 곱의 최소 연산수
    dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    # 해당 행렬은 0으로 초기화
    for i in range(1, n+1):
        dp[i][i] = 0
    # 2개씩 일단 초기화 한다.
    for i in range(1, n):
        dp[i][i+1] = ms[i-1][0] * ms[i-1][1] * ms[i][1]

    # 확인할 행렬의 개수
    for w in range(2, n):
        # 시작 행렬 번호
        for i in range(1, n-w+1):
            # i번째 행렬포함 w개 행렬곱의 최솟값을 구한다.
            for j in range(i+1, i+w+1):
                sum = dp[i][j-1] + dp[j][i+w] + ms[i-1][0] * ms[j-2][1] * ms[i+w-1][1]
                dp[i][i+w] = min(dp[i][i+w], sum)
    
    return dp[1][n]

# 이 문제는 전부 확인해야 하는 문제였다.
# 행렬의 순서들은 고정이고 계산 순서만 확인하는 방식
# 그래서 dp를 생각했고 2개씩 확인하는 경우부터 n개를 확인하는 경우까지 계산한다.
# 따라서 dp중에서도 바텀업 방식을 택했고 이에 맞게 코드를 작성했다.