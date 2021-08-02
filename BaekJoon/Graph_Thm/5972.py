import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
shed = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    shed[a].append((b, c))
    shed[b].append((a, c))

def di(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for i in shed[node]:
            c = d + i[1]
            if c < dist[i[0]]:
                dist[i[0]] = c
                heapq.heappush(q, (c, i[0]))
di(1)
print(dist[n])
# 전형적인 다익스트라 문제.