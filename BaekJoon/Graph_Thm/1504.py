import sys, heapq

def dijkstra(x, a, b):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, [0, x])
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance[a], distance[b]

n, e = map(int, input().split())
INF = float('inf')
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
# 꼭 거처야 하는 두 정점 v1, v2라 하면
# 1 -> v1 -> v2 -> n
# 1 -> v2 -> v1 -> n 이 두 가지가 있다.
# 그러니 일단 1, v1, v2 3개를 다익스트라 돌리고 저 두가지중에 최소를 답으로 도출.

start_to_v1, start_to_v2 = dijkstra(1, v1, v2)
v1_to_v2, v1_to_N = dijkstra(v1, v2, n)
v2_to_v1, v2_to_N = dijkstra(v2, v1, n)

res = min(start_to_v1 + v1_to_v2 + v2_to_N, start_to_v2 + v2_to_v1 + v1_to_N)
print(res if res != INF else -1)