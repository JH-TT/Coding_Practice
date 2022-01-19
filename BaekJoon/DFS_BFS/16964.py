import sys
input = sys.stdin.readline

def dfs(N, lv):
    if visit[N]:
        return 0
    visit[N] = 1
    s = 1
    level[N] = lv
    for node in edge[N]:
        s += dfs(node, lv+1)
    size[N] = s
    return s


n = int(input())
edge = [[] for _ in range(n + 1)]
level = [0] * (n + 1)
visit = [0] * (n + 1)
size = [0] * (n + 1)

for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
seq = list(map(int, input().split()))

if seq[0] != 1:
    print(0)
else:
    dfs(1, 0)
    for i in range(1, n):
        node = seq[i]
        if size[node] == 1 or i + size[node] >= n:
            continue
        next = seq[i + size[node]]
        if level[next] > level[node]:
            print(0)
            exit(0)
    print(1)

# dfs에 위반되는 상황
# 자식이 부모보다 먼저 나오는 경우가 있어서는 안된다.
# 특징 : i번째 등장하는 노드 x의 깊이는 어떤 순서 i+x의 서브트리의 크기까지는 전부 그 노드의 자식이라는 점이다.

# 참고 사이트 : https://blog.joonas.io/94