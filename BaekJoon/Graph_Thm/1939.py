from collections import deque
import sys
input = sys.stdin.readline

def bfs(mid):
    visit[s] = 1
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        if now == e:
            return True
        for i in graph[now]:
            if not visit[i[0]] and mid <= i[1]:
                visit[i[0]] = 1
                q.append(i[0])

    return False
                

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, e = map(int, input().split())

l, h = 1, 1000000000
while l <= h:
    visit = [0] * (n + 1)
    mid = (l + h) // 2
    if bfs(mid):
        l = mid+1
    else:
        h = mid-1
print(h)

# BFS와 이진탐색을 이용해서 품
# 다익스트라도 되는데 조건이 좀 까다로운듯