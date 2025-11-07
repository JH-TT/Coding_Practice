import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    xa = find_parent(parent, a)
    xb = find_parent(parent, b)

    if xa < xb:
        parent[xb] = xa
    else:
        parent[xa] = xb

n, m = map(int, input().split())

parent = [i for i in range(n)]
cnt = 0
find_flag = False
for _ in range(m):
    a, b = map(int, input().split())
    cnt += 1
    if find_parent(parent, a) == find_parent(parent, b):
        find_flag = True
        break
    else:
        union_parent(parent, a, b)

print(cnt if find_flag else 0)

# 전형적인 사이클문제