import heapq
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

q = []
heapq.heappush(q, a[0])
res = []

for i in a[1:]:
    if i[0] <= q[0][1]:
        if i[1] > q[0][1]:
            a, b = heapq.heappop(q)
            heapq.heappush(q, [a, i[1]])
        continue
    else:
        if q:
            x, y = heapq.heappop(q)
            res.append(y - x)
        heapq.heappush(q, i)
while q:
    a, b = heapq.heappop(q)
    res.append(b - a)
print(sum(res))

# 이 문제는 11000과 알고리즘이 비슷함. 대신 이건 입력이 정렬된 상태로 입력되기 때문에 정렬할 필요x