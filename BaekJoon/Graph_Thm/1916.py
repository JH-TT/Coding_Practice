import sys, heapq
input = sys.stdin.readline
INF = 10**10

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
dist[start] = 0
while q:
    d, now = heapq.heappop(q)
  
    if dist[now] < d:
        continue
      
    for next in graph[now]:
        cost = next[1] + d
        if cost >= dist[next[0]]:
            continue
        dist[next[0]] = cost
        if next[0] == end:
            continue
        heapq.heappush(q, (cost, next[0]))
print(dist[end])

# cost > dist[next[0]] 으로 했을때 메모리 초과가 떴다.
# >를 >=로 바꿔주니 통과했고, 또한 next노드가 end노드면 continue를 넣어 더 줄일 수 있다.