from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
visit = [[0 for _ in range(m)] for _ in range(n)]
campus = []
q = deque()

for i in range(n):
    cam = input().rstrip()
    for j in range(m):
        if cam[j] == "I":
            q.append((i, j))
            visit[i][j] = 1
    campus.append(cam)

friends = 0
while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if visit[nx][ny] == 1:
            continue

        if campus[nx][ny] == "X":
            continue

        if campus[nx][ny] == "P":
            friends += 1

        visit[nx][ny] = 1
        q.append((nx, ny))

print(friends if friends > 0 else "TT")

# 기본적인 BFS 문제