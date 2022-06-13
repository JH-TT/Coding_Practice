def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % div
    return temp

div = 1000000007

n = int(input())

ans = [[1, 0], [0, 1]]
a = [[1, 1], [1, 0]]

while n > 0:
    if n % 2 == 1:
        ans = multi(ans, a)
    a = multi(a, a)
    n //= 2

print(ans[0][1])

# 분할 정복을 이용한 거듭제곱 이용.
# 홀수면 한 개는 빼놓고 짝수개는 제곱을 이용해서 n/2 번만에 계산 후 빼놓은 한 개 곱함.