def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
edge = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append([c, a, b])

parent = [i for i in range(v+1)]
edge.sort()

cost = 0

for i in edge:
    c, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        cost += c
print(cost)

# MST 기본문제