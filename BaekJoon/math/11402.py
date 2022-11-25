binomial = [[0] * 2010 for _ in range(2010)]

n, k, m = map(int, input().split())

for i in range(m):
    binomial[i][0] = 1
    for j in range(1, i+1):
        binomial[i][j] = (binomial[i-1][j-1] + binomial[i-1][j]) % m

ret = 1
while n or k:
    ret *= binomial[n%m][k%m]
    n //= m
    k //= m
    ret %= m
print(ret)

# https://bowbowbow.tistory.com/2