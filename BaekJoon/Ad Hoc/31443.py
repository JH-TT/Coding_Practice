n, m = map(int, input().split())

size = n * m
res = 1
MOD = 10 ** 9 + 7

while size > 4:
    res *= 3
    res %= MOD
    size -= 3

res *= size

print(res % MOD)

# 크기가 n인 조각을 s의 크기로 나눌때 가장 큰 수가 되도록 하는 s
# 이때 s는 자연로그 e에 가까워지기 때문에 정수중에 e에 가까운 숫자인 3을 기준으로 계산.
# 4의 경우는 2로 나누는게 더 크기 때문에 4보다 클때까지만 3으로 계산하고 마지막엔 나머지를 곱하도록 구현