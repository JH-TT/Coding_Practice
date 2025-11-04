import sys
from collections import defaultdict

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def CCW(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

parent = [i for i in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if find_parent(parent, i) != find_parent(parent, j):
            x1, y1, x2, y2 = lines[i]
            x3, y3, x4, y4 = lines[j]
            first_condition = CCW([x1, y1], [x2, y2], [x3, y3]) * CCW([x1, y1], [x2, y2], [x4, y4])
            second_condition = CCW([x3, y3], [x4, y4], [x1, y1]) * CCW([x3, y3], [x4, y4], [x2, y2])
            if first_condition == 0 and second_condition == 0:
                third = (min(x1, x2) <= max(x3, x4) and
                         min(x3, x4) <= max(x1, x2) and
                         min(y1, y2) <= max(y3, y4) and
                         min(y3, y4) <= max(y1, y2))
                if third:
                    union(parent, i, j)
                continue

            if first_condition <= 0 and second_condition <= 0:
                union(parent, i, j)

for i in range(n):
    find_parent(parent, i)

cnt = defaultdict(int)
for i in range(n):
    cnt[parent[i]] += 1

res = max([cnt[x] for x in cnt.keys()])

print(len(cnt))
print(res)

# union_find인데 기존 union_find는 노드들 기준이라면 이 문제는 선분으로 바뀐정도
# 서로 교차하면 union을 진행하도록 한다