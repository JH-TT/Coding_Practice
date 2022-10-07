# 틀렸다고 나옴. 하지만 반례는 아직도 못찾음...
import sys
input = sys.stdin.readline

n = int(input())
crane = sorted(list(map(int, input().split())))
m = int(input())
boxes = list(map(int, input().split()))

if max(boxes) > crane[-1]:
    print(-1)
    exit(0)

dp = [0] * n
for box in boxes:
    for i in range(n):
        if box <= crane[i]:
            dp[i] += 1
            break

# dp = [100, 1, 1, 1, 1, 1]
# n = len(dp)

res = 0
while sum(dp) > 0:
    print(dp)
    idx2 = n-1
    for i in range(n-1, -1, -1):
        if dp[i] > 0:
            k = (dp[i] // (n-i)) + (dp[i] % (n-i) != 0)
            dp[i] = 0
            idx2 = i-1
            break
    res += k
    total = k
    for i in range(idx2, -1, -1):
        if dp[i] == 0:
            total += k
            continue
        if dp[i] < total:
            total -= dp[i]
            dp[i] = 0
        else:
            dp[i] -= total
            total = 0
        total += k
print(res)

# 정답
import sys

read = sys.stdin.readline

N = int(read())
cranes = list(map(int, read().split()))

M = int(read())
boxs = list(map(int, read().split()))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

if boxs[0] > cranes[0]:
    print(-1)
    sys.exit()
else:
    time = 0

    while boxs:
        if not boxs:
            break

        for crane in cranes:
            for box in boxs:
                if crane >= box:
                    boxs.remove(box)
                    break

        time += 1

    print(time)