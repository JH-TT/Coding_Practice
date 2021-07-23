from collections import deque
import sys
sys.setrecursionlimit(10**6) # dfs같은 경우는 보통 재귀함수 깊이가 낮아서 써주는게 좋음.
input = sys.stdin.readline

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n + 1):
    graph[i].sort()


visit_d = [False] * (n + 1) # dfs에 대한 visit
visit_b = [False] * (n + 1) # bfs에 대한 visit

def dfs(graph, v, visit_d):
    visit_d[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visit_d[i]:
            dfs(graph, i, visit_d)

def bfs(graph, start, visit_b):
    q = deque([start])
    visit_b[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visit_b[i]:
                q.append(i)
                visit_b[i] = True

dfs(graph, start, visit_d)
print()
bfs(graph, start, visit_b)