from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

visit = [[[-1, -1] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b, 0))
    visit[a][b][0] = 1
    while q:
        a, b, c = q.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][c]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            z = c
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if maze[x][y] == 0 and visit[x][y][z] == -1:
                visit[x][y][z] = visit[a][b][c] + 1
                q.append((x, y, z))
            if maze[x][y] == 1 and z == 0:
                z = 1
                if visit[x][y][z] == -1:
                    visit[x][y][z] = visit[a][b][c] + 1
                    q.append((x, y, z))
    return -1
print(bfs(0, 0))
# 내 DFS_BFS에서 escapemaze코드와 거의 동일. 문제도 같음.
# BFS에 놓는게 맞지만 그냥 그래프이론이 개수가 적길래 여기다 넣음.