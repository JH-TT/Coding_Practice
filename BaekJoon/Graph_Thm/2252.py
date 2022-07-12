from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n + 1)
edge = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    edge[a].append(b)


q = deque()
res = []
for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

while q:
    node = q.popleft()
    res.append(node)
    for i in edge[node]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)
print(*res)

# 위상정렬 standard 문제
# 보통 2개만 비교해서 크기 순서를 정할때는 위상정렬을 이용.