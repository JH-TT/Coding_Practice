# 다익스트라 알고리즘(최단경로 찾을 때)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정.

# 노드개수 : v, 간선의 개수 : e
v, e = map(int, input().split())

# 시작노드 : k
k = int(input())

# 각 노드와 연결되어 있는 노드에 대한 정보를 담는 리스트 생성.
graph = [[] for _ in range(v + 1)]
# 거리를 무한대로 초기화
distance = [INF] * (v + 1)

# 노드의 정보를 입력.
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘.
def short(start):
    q = []
    # 힙은 첫번째 값을 기준으로 구성하기 때문에, 거리를 첫번째 원소에 넣는다.
    heapq.heappush(q, (0, start))
    distance[start] = 0 # 시작노드 자신은 거리가 0.
    # q가 빌때까지 반복.
    while q:
        # 거리와 현재 노드 pop.
        dist, now = heapq.heappop(q)
        # 이미 들렸던 노드면 무시.
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

short(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])