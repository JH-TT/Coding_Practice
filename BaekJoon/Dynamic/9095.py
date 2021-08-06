T = int(input())

for _ in range(T):
    n = int(input())
    arr = [0] * 11
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(4, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3] # 1을 더하는 경우 + 2를 더하는 경우 + 3을 더하는 경우
    print(arr[n])

# 간단한 DP문제