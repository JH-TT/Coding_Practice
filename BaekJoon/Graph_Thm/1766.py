import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
q = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    p = heapq.heappop(q)
    print(p, end = " ")
    for i in graph[p]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

# 일반적인 위상정렬 + 우선순위 큐를 이용하는 문제. heapq만 썼음