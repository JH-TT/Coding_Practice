# 내 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n, cnt, start):  
    # 만난 노드의 값의 차가 2이상이면 사이클 발생.
    for node in edge[n]:
        if visit[node] and cnt - visit[node] >= 2:
            answer[start-1] = visit[node] - 1
            return
            
        if not visit[node]:
            visit[node] = cnt + 1
            dfs(node, cnt+1, start)
    

n = int(input())
edge = [[] for _ in range(n + 1)]
answer = [0] * n
for _ in range(n):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(1, n+1):
    visit = [0] * (n + 1)
    visit[i] = 1
    dfs(i, 1, i)

print(*answer)

# 다른사람 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(cv,pv):
    if cache[cv] == 1: return cv
    cache[cv] = 1

    for nv in grid[cv]:
        if nv == pv: continue  # 양방향 그래프기 때문
        result = dfs(nv,cv)
        if result >= 0:
            cache[cv] = 2
            return result if cv != result else -1

    return -1


def bfs():
    q = []
    for i in range(n):
        if cache[i] == 2: 
            q.append(i)
            dist[i] = 0

    while q:
        tmp = []

        for cv in q:
            for nv in grid[cv]:
                if dist[nv] != -1: continue
                dist[nv] = dist[cv] + 1
                tmp.append(nv)

        q = tmp



n = int(input())
grid = [[] for _ in range(n)]
cache = [0]*n
dist = [-1]*n

for _ in range(n):
    a,b = map(int, input().split())
    grid[a-1].append(b-1)
    grid[b-1].append(a-1)

dfs(0,-1)
bfs()
print(*dist)