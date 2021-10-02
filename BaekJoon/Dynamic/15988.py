import sys
input = sys.stdin.readline

T = int(input())

cnt = [0] * 1000001

cnt[1] = 1
cnt[2] = 2
cnt[3] = 4

for i in range(4, 1000001):
    cnt[i] = sum(cnt[i-3:i]) % 1000000009

for _ in range(T):
    n = int(input())
    print(cnt[n])

# 하나씩 해보면 n >= 4 인경우에는 n-1, n-2, n-3 의 개수의 합이 됨을 바로 볼 수 있다.