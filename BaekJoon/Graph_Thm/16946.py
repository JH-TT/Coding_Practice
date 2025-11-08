from collections import deque
import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    xa = find_parent(a)
    xb = find_parent(b)

    if xa < xb:
        parent[xb] = xa
        area[xa] += area[xb]
    else:
        parent[xa] = xb
        area[xb] += area[xa]

def pos_to_num(x, y):
    return x * m + y

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        origin = pos_to_num(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visit[nx][ny]:
                continue

            if arr[nx][ny] == '1':
                continue

            nxt_pos = pos_to_num(nx, ny)
            if find_parent(origin) == find_parent(nxt_pos):
                continue

            visit[nx][ny] = True
            union_parent(origin, nxt_pos)
            q.append((nx, ny))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

arr = [list(input())[:-1] for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
parent = [i for i in range(n * m)]
area = [1 if arr[i // m][i % m] == '0' else 0 for i in range(n * m)]

walls = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            walls.append((i, j))
            visit[i][j] = True
            continue
        if visit[i][j]:
            continue
        visit[i][j] = True
        bfs(i, j)

for wall in walls:
    x, y = wall
    cnt = 1
    all_groups = set()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        all_groups.add(find_parent(pos_to_num(nx, ny)))

    for group in all_groups:
        cnt += area[group]

    arr[x][y] = str(cnt % 10)

for a in arr:
    print(''.join(a))

# 일단 벽 좌표는 따로 모아두면서 벽이 아닌 애들은 인접한 애들끼리 묶어서 그룹지어놓는다. 이는 경로압축같은걸 이용해서 그룹짓는다.
# 아까 모아둔 벽 좌표를 for loop 돌면서 벽에 인접한 그룹의 크기를 더하는 방식으로 한다.
# 일단 각 리스트가 최대 100만개이기 때문에 메모리적으로는 충분하기 때문에 그냥 리스트 이용함.
# line 79번에 그룹을 set을 이용했는데, 이유는 상하좌우로 인접했다고 바로 그룹의 크기를 더해버리면 같은 그룹을 중복으로 더하는 상황이 발생할 수 있으니 set으로 중복제거를 한 뒤에 따로 진행했다.