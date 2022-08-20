import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(a, d):
    for node, cost in edge[a]:
        if visit[node] == -1:
            visit[node] = d + cost
            dfs(node, d + cost)

n = int(input())

edge = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    edge[a].append([b, c])
    edge[b].append([a, c])

visit = [-1] * (n + 1)
visit[1] = 0
dfs(1, 0)

start = visit.index(max(visit))
visit = [-1] * (n + 1)
visit[start] = 0
dfs(start , 0)
print(max(visit))

# 전형적인 트리의 지름 문제.
# 한 노드로부터 가장 먼 노드를 찾는다.
# 그 노드에서 다시 가장 먼 노드를 찾고 길이를 구한다. 그것이 트리의 지름이 된다.