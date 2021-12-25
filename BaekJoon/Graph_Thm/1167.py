import sys
input = sys.stdin.readline

def dfs(node):
    for n, c in edge[node]:
        if visit[n] == 0:
            visit[n] = visit[node] + c
            dfs(n)

n = int(input())

edge = [[] for _ in range(n + 1)]

for _ in range(n):
    node, *info = map(int, input().split())
    i = 0
    while i != len(info) - 1:
        edge[node].append([info[i], info[i + 1]])
        i += 2

visit = [0 for _ in range(n + 1)]
dfs(1)
visit[1] = 0
idx = visit.index(max(visit))

visit = [0 for _ in range(n + 1)]
dfs(idx)
visit[idx] = 0
print(max(visit))

# 트리의 지름 구하는 방법.
# 1. 아무 노드(a)에서 가장 멀리있는 노드(b)를 구한다.
# 2. 그 노드(b)에서 가장 먼 노드(c)까지 길이가 트리의 지름이 된다.