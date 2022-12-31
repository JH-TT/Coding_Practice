import sys, heapq
input = sys.stdin.readline

def distance(cor1, cor2):
    return ((cor1[0]-cor2[0])**2 + (cor1[1]-cor2[1])**2) ** 0.5

n, w = map(int, input().split())
m = float(input())
INF = sys.maxsize

cor = [[0, 0]]
graph = [[] for _ in range(n+1)]

for _ in range(n):
    cor.append(list(map(int, input().split())))

# 거리가 m을 넘지 않으면 정보를 넣는다.
for i in range(1, n+1):
    for j in range(i+1, n+1):
        d = distance(cor[i], cor[j])
        if d <= m:
            graph[i].append([j, d])
            graph[j].append([i, d])

# 이미 연결된 노드끼리는 거리가 0 이전에 값이 있어도 거리를 0으로 두면 결국 덮어씌워진다.
for _ in range(w):
    a, b = map(int, input().split())
    graph[a].append([b, 0])
    graph[b].append([a, 0])

# 다익스트라 기본 코드
def dijkstra():
    dist = [INF for _ in range(n+1)]
    dist[1] = 0
    q = []
    heapq.heappush(q, [0, 1])
    while q:
        cost, node = heapq.heappop(q)

        if dist[node] < cost:
            continue
        for next in graph[node]:
            if next[1] + cost < dist[next[0]]:
                dist[next[0]] = next[1] + cost
                heapq.heappush(q, [next[1]+cost, next[0]])
    return int(dist[n]*1000)
print(dijkstra())