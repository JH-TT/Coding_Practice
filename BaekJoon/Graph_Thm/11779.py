import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

INF = sys.maxsize
visit = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a -> b로가는데 비용 c가 든다.

start, end = map(int, input().split())
# 힙에 필요한 정보: 현재위치, 누적비용, 트랙
q = []
visit[start] = 0
heapq.heappush(q, (0, start, [start])) # 비용을 첫 번째 인덱스에 넣어야 비용 기준으로 힙이 진행된다.

while q:
    cost, now, path = heapq.heappop(q)

    if now == end:
        print(cost)
        print(len(path))
        print(*path)
        break

    for nxt, c in graph[now]:
        if visit[nxt] <= cost + c:
            continue
        visit[nxt] = cost + c
        heapq.heappush(q, (cost + c, nxt, path + [nxt]))

# 기존 다익스트라 로직에서 매개변수인 path를 추가해 경로까지 가져오도록 함.