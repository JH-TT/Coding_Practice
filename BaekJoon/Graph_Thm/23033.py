import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]
for _ in range(m):
    a, b, t, w = map(int, input().split())
    graph[a].append((b, t, w))


q = []
distance[1] = 0
heapq.heappush(q, (0, 1)) # (현재 거리, 현재 노드
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for nxt in graph[now]:
        cost = dist + nxt[1]
        if dist % nxt[2] != 0:
            cost += (nxt[2] - dist % nxt[2])
        if cost < distance[nxt[0]]:
            distance[nxt[0]] = cost
            heapq.heappush(q, (cost, nxt[0]))

print(distance[n])

# 기본적인 다익스트라에 기차를 기다리는 시간이 추가된정도의 난이도.