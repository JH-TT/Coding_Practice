MOD = 1000000000
MAX = (1 << 10) - 1

def stair():
    # dp[마지막으로 끝나는 숫자][현재비트마스킹]
    dp = [[0] * (MAX + 1) for _ in range(10)]

    for i in range(1, 10):
        dp[i][1 << i] = 1
    # N번 반복
    for _ in range(2, N + 1):
        next_dp = [[0] * (MAX + 1) for _ in range(10)]

        for i in range(10):
            for j in range(MAX + 1):
                # 1이상 8이하면 앞뒤확인, 0은 1만, 9는 8만 확인
                if i > 0:
                    next_dp[i][j | (1 << i)] = (next_dp[i][j | (1 << i)] + dp[i - 1][j]) % MOD
                if i < 9:
                    next_dp[i][j | (1 << i)] = (next_dp[i][j | (1 << i)] + dp[i + 1][j]) % MOD
                  
        dp = next_dp # dp갱신해줌.


    return sum(dp[i][MAX] for i in range(10)) % MOD

N = int(input())
print(stair())


# 참고 : https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-1562%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%88%98