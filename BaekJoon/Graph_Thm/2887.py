import heapq, sys
input = sys.stdin.readline

n = int(input())

points = []
for i in range(n):
    x, y, z = map(int, input().split())
    points.append((x, y, z, i)) # x, y, z좌표랑 i번째 행성

points_x = sorted(points, key = lambda p: p[0])
points_y = sorted(points, key = lambda p: p[1])
points_z = sorted(points, key = lambda p: p[2])

edges = []
for i in range(n-1):
    *p1, pn1 = points_x[i]
    *p2, pn2 = points_x[i + 1]

    edges.append((pn1, pn2, min([abs(p1[j] - p2[j]) for j in range(3)])))

for i in range(n-1):
    *p1, pn1 = points_y[i]
    *p2, pn2 = points_y[i + 1]

    edges.append((pn1, pn2, min([abs(p1[j] - p2[j]) for j in range(3)])))

for i in range(n-1):
    *p1, pn1 = points_z[i]
    *p2, pn2 = points_z[i + 1]

    edges.append((pn1, pn2, min([abs(p1[j] - p2[j]) for j in range(3)])))

edges.sort(key=lambda e: e[2])

parent = [i for i in range(n)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

res = 0
for a, b, cost in edges:
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        res += cost

print(res)

# 이 문제는 간선이 따로 주어지지않은 문제
# n의 범위가 10만이라 단순히 모든 간선을 확인할 수 없다.
# **간선의 개수를 줄이는게 핵심**
# 비용이 적으면 되니까 x, y, z좌표 각각 정렬해서 인접한 행성들을 간선의 후보로 정한다.
#     이러면 많아봐야 각 행성마다 3개의 간선이 존재할 것이다.
# MST 알고리즘을 실행한다.