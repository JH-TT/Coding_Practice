# 보텀업 방식.

import sys
sys.setrecursionlimit(10**6)

n = int(input())

num = [0] * (10**6 + 1)

for i in range(2, n + 1):
    # 현재의 수에서 1을 때는 경우 (1을 더하는 이유는 호출 횟수를 구해야하기 때문 2로 나누는것과 3부분도 같은 이유.)
    num[i] = num[i - 1] + 1
    # 2로 나누어 떨어지는 경우.
    if i % 2 == 0:
        num[i] = min(num[i], num[i // 2] + 1)
    # 3으로 나누어 떨어지는 경우.
    if i % 3 == 0:
        num[i] = min(num[i], num[i // 3] + 1)
print(num[n])