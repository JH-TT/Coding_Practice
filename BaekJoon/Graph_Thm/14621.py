import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
school = [""] + list(input().split())

graph = []
parent = list(range(N + 1))
res = 0
edges = 0

for _ in range(M):
    u, v, d = map(int, input().split())
    graph.append((d, u, v))
graph.sort()

for i in graph:
    cost, a, b = i

    if school[a] == school[b]: # 같은 종류의 학교는 연결 x
        continue

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        edges += 1 # 간선 추가

print(res if edges == N - 1 else -1) # 간선의 개수가 N - 1이면 전부 연결됐다는 의미 아니면 모두 연결 안됨.