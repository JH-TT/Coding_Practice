from collections import defaultdict
import sys
input = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)

    if px < py:
        parent[py] = px
        cnt[px] += cnt[py]
    else:
        parent[px] = py
        cnt[py] += cnt[px]

T = int(input())
for _ in range(T):
    F = int(input())

    relation = defaultdict(int)
    parent = [i for i in range(200001)]
    cnt = [1 for _ in range(200001)]

    i = 1
    for _ in range(F):
        a, b = input().split()

        if a not in relation:
            relation[a] = i
            i += 1

        if b not in relation:
            relation[b] = i
            i += 1

        if find_parent(relation[a]) != find_parent(relation[b]):
            union_parent(relation[a], relation[b])
        print(cnt[find_parent(relation[a])])

# 그냥 서로소 문제인데 단순히 키가 문자열이된 것뿐...