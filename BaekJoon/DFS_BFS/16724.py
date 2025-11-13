# N X M에 대한 사이클 개수 구하기
from collections import deque
import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def get_num(x, y):
    return x * m + y

n, m = map(int, input().split())

dir = [list(input())[:-1] for _ in range(n)]
visit = [[False] * m for _ in range(n)]
parent =[i for i in range(n * m)]

cycle = 0
for i in range(n):
    for j in range(m):
        if visit[i][j]:
            continue
        q = deque()
        q.append((i, j))
        visit[i][j] = True

        while q:
            x, y = q.popleft()

            if dir[x][y] == 'D':
                nx = x + 1
                ny = y
            elif dir[x][y] == 'U':
                nx = x - 1
                ny = y
            elif dir[x][y] == 'L':
                nx = x
                ny = y - 1
            else:
                nx = x
                ny = y + 1

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            union_parent(get_num(x, y), get_num(nx, ny))

            if visit[nx][ny]:
                continue

            visit[nx][ny] = True
            q.append((nx, ny))

for i in range(n * m):
    find_parent(i)

res = set()
for p in parent:
    res.add(p)

print(len(res))
# union-find로 푼 문제


# DFS로 푼 문제
# 상태를 3개로 (미방문, 방문중, 방문완료) 둬서 사이클의 개수를 구한다.
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

# 방문 상태: 0 = 미방문, 1 = 방문 중, 2 = 방문 완료
state = [[0] * m for _ in range(n)]

# 방향 매핑
dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

result = 0


def dfs(x, y):
    global result
    state[x][y] = 1  # 방문 중

    nx = x + dx[board[x][y]]
    ny = y + dy[board[x][y]]

    if state[nx][ny] == 0:
        # 아직 방문 안했으면 계속 DFS
        dfs(nx, ny)
    elif state[nx][ny] == 1:
        # 방문 중인 곳을 다시 방문 → 사이클 발견!!
        result += 1
    # state[nx][ny] == 2 → 이미 처리된 경로면 아무것도 하지 않음

    state[x][y] = 2  # 탐색 완료


for i in range(n):
    for j in range(m):
        if state[i][j] == 0:
            dfs(i, j)

print(result)