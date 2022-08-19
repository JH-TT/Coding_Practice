# Pypy3로 통과
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n-i):
        x = j + i
        dp[j][x] = float('inf')
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + arr[j][0] * arr[k][1] * arr[x][1])

print(dp[0][-1])

# a b c d 행렬이 있으면
# a + bcd + 계산값 or ab + cd + 계산값 or abc + d + 계산값 이렇게 나뉜다.
# 이 부분이 3중반복문 가장 깊은곳에 있는 부분. 저 중에 최소가 돼야한다.
# ref : https://pacific-ocean.tistory.com/437
# ref : https://rccode.tistory.com/155