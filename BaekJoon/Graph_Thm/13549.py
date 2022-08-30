# 다익스트라
import heapq

n, k = map(int, input().split())
INF = float('inf')
graph = [[] for _ in range(100001)]
distance = [INF] * (100001)

for i in range(100001):
    if i == 0:
        graph[i].append((i+1, 1))
    elif i == 100000:
        graph[i].append((i-1, 1))
    else:
        graph[i].append((i-1, 1))
        graph[i].append((i+1, 1))
        if i * 2 <= 100000:
            graph[i].append((i*2, 0))

q = []
heapq.heappush(q, (0, n))
distance[n] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = i[1] + dist
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
print(distance[k])

# bfs 더 빠름
from collections import deque
INF = 100001
visit = [False] * INF
dist = [-1] * INF

n, k = map(int, input().split())
q = deque()
q.append(n)
visit[n] = True
dist[n] = 0

while q:
    now = q.popleft()
    if now*2 < INF and visit[now*2] == False:
        q.appendleft(now*2)
        visit[now*2] = True
        dist[now*2] = dist[now]
    if now+1 < INF and visit[now+1] == False:
        q.append(now+1)
        visit[now+1] = True
        dist[now+1] = dist[now]+1
    if now-1 >= 0 and visit[now-1] == False:
        q.append(now-1)
        visit[now-1] = True
        dist[now-1] = dist[now]+1
print(dist[k])

# 이 문제를 풀기위한 방법
# 다익스트라(내 풀이)
# 0-1 bfs 참고(https://velog.io/@aonee/%EB%B0%B1%EC%A4%80-boj-13549-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%883-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
# * 2를 별도의 간선으로 생각하지 않고, +1이나 -1에 의한 좌표를 큐에 넣을 때 그 좌표의 2의 거듭제곱 배인 좌표들을 전부 큐에 넣는 방법