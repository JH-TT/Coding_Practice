import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

n, m, k, x = map(int, input().split())
city = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

def di(start):
    global dist
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in city[now]:
            if d + 1 < dist[i]:
                dist[i] = d + 1
                heapq.heappush(q, (dist[i], i))
di(x)

flag = False
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        flag = True
if not flag:
    print(-1)

# 그냥 전형적인 다익스트라 코드이고, 다만 마지막에 거리가 k인 도시가 없으면 -1을 출력하도록 했음.