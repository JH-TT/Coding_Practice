# 1654번이랑 같은문제. 다만 시간제한이 이 문제는 1초.

n, k = map(int, input().split())

a = []

for _ in range(n):
    a.append(int(input()))

s = 0
e = max(a)

res = 0
while s <= e:
    m = (s + e) // 2
    t = sum(i//m for i in a)
    if t < k:
        e = m - 1
    else:
        s = m + 1
print(e)