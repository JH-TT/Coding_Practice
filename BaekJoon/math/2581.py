import math, sys

m = int(input())
n = int(input())

eratos = [1] * (n + 1)
eratos[1] = 0
for i in range(2, int(math.sqrt(n)) + 1):
    j = 2
    while i * j <= n:
        eratos[i*j] = 0
        j += 1

total = 0
mini = sys.maxsize
for i in range(m, n+1):
    total += i * eratos[i]
    mini = min(mini, i) if eratos[i] else mini
if total:
    print(total)
    print(mini)
else:
    print(-1)

# 에라토스 기본문제