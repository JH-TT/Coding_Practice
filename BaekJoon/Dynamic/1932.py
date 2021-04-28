n = int(input())

num = []
for _ in range(n):
    b = [0]
    b += list(map(int, input().split()))
    b += [0]
    num.append(b)

for i in range(1, n):
    for j in range(1, len(num[i]) - 1):
        num[i][j] = num[i][j] + max(num[i - 1][j - 1], num[i - 1][j]) # 왼쪽 대각선이랑 오른쪽 대각선 중에 더 큰 값을 더한다.
print(max(num[n - 1]))