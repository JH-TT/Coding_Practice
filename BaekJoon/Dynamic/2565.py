import sys
input = sys.stdin.readline

n = int(input())
res = [1] * n
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr = sorted(arr, key=lambda x : x[0])

for i in range(1, n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            res[i] = max(res[i], res[j] + 1)
print(n - max(res))

# 전형적인 LIS 문제.