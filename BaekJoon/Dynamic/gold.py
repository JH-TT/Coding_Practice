n, m = map(int, input().split())
gold = [[0] * (m + 2) for _ in range(n + 2)]
a = list(map(int, input().split()))
k = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        gold[i][j] = a[k]
        k += 1

for j in range(2, m + 1):
    for i in range(1, n + 1):
        gold[i][j] = gold[i][j] + max(gold[i][j - 1], gold[i - 1][j - 1], gold[i + 1][j - 1]) # 왼쪽에서 오는거, 왼쪽 위에서 오는거, 왼쪽 아래에서 오는것중 최댓값.

big = 0
for i in range(1, n + 1):
    big = max(big, gold[i][m])
print(big)