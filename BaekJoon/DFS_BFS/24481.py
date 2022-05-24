import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(tree, v, cnt, visited):
    ans[v] = cnt    
    visited[v] = True
    for i in tree[v]:
        if not visited[i]:        
            dfs(tree, i, cnt+1, visited)

n, m, r = map(int, input().split())
visited = [False for i in range(n+1)]

ans = [-1 for i in range(n + 1)]
tree = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1, n+1):
    tree[i].sort()  

dfs(tree, r, 0, visited)
print(*ans[1:], sep="\n")