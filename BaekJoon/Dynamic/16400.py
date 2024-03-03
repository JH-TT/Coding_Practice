n = int(input())

eratos = [True] * (n + 1)
eratos[0] = eratos[1] = False
for i in range(2, int((n + 1) ** 0.5) + 1):
    if eratos[i]:
        j = 2
        while i * j <= n:
            eratos[i * j] = False
            j += 1

p = [i for i in range(1, n + 1) if eratos[i]] # 소수만 적어놓기

dp = [0] * (n + 1)
dp[0] = 1

for i in p:
    for j in range(i, n + 1):
        dp[j] += dp[j-i]
        dp[j] %= 123456789
print(dp)

# 이전에 비슷한걸 풀었었는데 까먹었음... 아직 멀었다 dp