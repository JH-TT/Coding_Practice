from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, *b = map(int, input().split())

    for i in range(len(b) - 1):
        graph[b[i]].append(b[i + 1])
        indegree[b[i + 1]] += 1

res = []
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    res.append(v)
    visited[v] = 1

    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(res) != n:
    print(0)
else:
    for i in res:
        print(i)

# 일반적인 위상정렬문제