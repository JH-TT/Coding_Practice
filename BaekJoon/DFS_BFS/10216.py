# bfs이용.
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
i = 1
a = []
e = [[0] for _ in range(3001)]
visit = [0] * 3001

def bfs(s):
    q = deque([s])
    visit[s] = 1
    while q:
        y = q.popleft()
        for i in e[y]:
            if not visit[i]:
                q.append(i)
                visit[i] = 1

while T:
    N = int(input())
    for i in range(N):
        x, y, r = map(int, input().split())
        a.append([x, y, r])
    
    for i in range(N):
        for j in range(i + 1, N):
            # 서로 연결돼 있는 사이라면 노드 연결
            dist = (a[i][0] - a[j][0]) * (a[i][0] - a[j][0]) + (a[i][1] - a[j][1]) * (a[i][1] - a[j][1])

            if dist <= (a[i][2] + a[j][2]) * (a[i][2] + a[j][2]):
                e[i].append(j)
                e[j].append(i)
    cnt = 0
    for i in range(N):
        if not visit[i]:
            bfs(i)
            cnt += 1
    print(cnt)
    a = []
    for i in range(N):
        e[i] = [0]
        visit[i] = 0
    T -= 1

# 서로소 집합 개수이용.
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])

    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def sol():
    ans = N
    parent = [i for i in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            x = a[i][0] - a[j][0]
            y = a[i][1] - a[j][1]
            r = a[i][2] + a[j][2]

            if (x**2) + (y**2) <= r**2:
                # 둘이 같은 부모노드가 아니면 union한다.
                if find_parent(parent, i) != find_parent(parent, j):
                    union_parent(parent, i, j)
                    ans -= 1
    return ans

T = int(input())

for _ in range(T):
    a = []
    N = int(input())
    for _ in range(N):
        x, y, r = map(int, input().split())
        a.append((x, y, r))

    print(sol())