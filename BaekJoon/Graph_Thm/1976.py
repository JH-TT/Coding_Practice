import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = list(range(n))

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:
            union_parent(parent, i, j)

track = list(map(int, input().split()))
flag = True
for i in range(m - 1):
    if parent[track[i] - 1] != parent[track[i + 1] - 1]:
        flag = False
        break
print("YES" if flag else "NO")

# 유니온 파인드로 한 집합내에 있는지 확인하면 되는 문제...
# 같은 집합에 있으면 각 노드끼리 이동이 가능하다는 의미


# BFS로 풀기
# 갈 수 있는지만 보면 되기 때문에 BFS로도 충분히 풀 수 있다.
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
track = list(map(int, input().split()))
visit = [False for _ in range(n)]

q = deque()
q.append(track[0] - 1)
visit[track[0] - 1] = True
while q:
    now = q.popleft()

    for i in range(n):
        if arr[now][i] and not visit[i]:
            visit[i] = True
            q.append(i)

flag = True
for t in track:
    if not visit[t - 1]:
        flag = False
        break
print("YES" if flag else "NO")