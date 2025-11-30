from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j, 0))
    visit = [[False for _ in range(c)] for _ in range(r)]
    visit[i][j] = True

    max_dist = 0
    while q:
        x, y, dist = q.popleft()

        max_dist = max(max_dist, dist)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if visit[nx][ny]:
                continue

            if arr[nx][ny] == 'W':
                continue

            visit[nx][ny] = True
            q.append((nx, ny, dist + 1))

    return res

dx = [0, 0, 1 ,-1]
dy = [1, -1, 0, 0]

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

res = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            continue
        res = max(res, bfs(i, j))

print(res)
# 모든 위치에서 BFS하는 문제