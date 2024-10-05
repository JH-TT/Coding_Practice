T = int(input())

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m + 1)]
    for c in coins:
        # 동전의 값 자체가 m보다 클 수 있으니 이때는 넘긴다.
        if c > m: break
        dp[c] += 1

        for j in range(c+1, m+1):
            dp[j] += dp[j - c]
    print(dp[m])