import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = -10000 * 40000 + 1

prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] + arr[i-1][j-1] - prefix[i-1][j-1]

for i in range(1, n+1):
    for j in range(1, m+1):
        for i2 in range(i, n+1):
            for j2 in range(j, m+1):
                res = max(res, prefix[i2][j2] - prefix[i-1][j2] - prefix[i2][j-1] + prefix[i-1][j-1])
print(res)

# 행렬을 직접 그려서 부분 행렬의 합을 어떻게 구하는지 생각해 보면서 하면 됨.(나름 자주 나오는 것임)