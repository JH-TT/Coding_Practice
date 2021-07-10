from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

def bfs(graph, start, visited):
    global flag
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1 # 인접한 노드들은 부모 노드와 다른 방문 계수로 업데이트.
            elif visited[v] == visited[i]: # 인접한 방문계수가 같으면 이분 그래프가 아님.
                return False
    return True

for _ in range(t):
    v, e = map(int, input().split())
    visited = [-1] + [0] * v
    graph = [[] for _ in range(v + 1)]
    flag = True
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:
            flag = bfs(graph, i, visited)
            if not flag:
                break

    print("YES" if flag else "NO")

# 이분탐색에 관한 내용 : https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html