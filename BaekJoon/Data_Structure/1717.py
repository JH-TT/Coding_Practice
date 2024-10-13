import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    p_a = find_parent(parent, a)
    p_b = find_parent(parent, b)

    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b
    return parent

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        parent = union_parent(parent, a, b)
    else:
        p_a = find_parent(parent, a)
        p_b = find_parent(parent, b)
        if p_a == p_b:
            print("YES")
        else:
            print("NO")
            
# 기본적인 union-find 문제