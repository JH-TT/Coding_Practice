import sys, heapq
input = sys.stdin.readline

def dijkstra(s):
    dist = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dist

INF = float('inf')
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

res = 0
x_dist = dijkstra(x) # x에서 각 집까지 최단거리

# 반복문 돌면서 각 사람을 시작점으로 다익스트라 실행.
for i in range(1, n + 1):
    if i == x:
        continue
    d = dijkstra(i)
    res = max(res, d[x] + x_dist[i]) # 왔다갔다하는 거리 최댓값 업데이트
print(res)