import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * (n + 1)

arr[1] = 1
arr[2] = 3

for i in range(3, n + 1):
    arr[i] = arr[i - 1] + arr[i - 2] * 2
print(arr[n] % 10007)

# 1자모양을 마지막에 놓는 경우 + =모양을 마지막에 놓는 경우 + ㅁ 모양을 마지막에 놓는경우