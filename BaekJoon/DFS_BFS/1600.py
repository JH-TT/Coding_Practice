from collections import deque
import sys
input = sys.stdin.readline

# 인접한 4방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 말 움직임
hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [1, -1, 2, -2, 2, -2, 1, -1]

k = int(input())
w, h = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(h)]

visit = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(k + 1)]
q = deque()
q.append((k, 0, 0))

while q:
    cnt, x, y = q.popleft()

    if x == h - 1 and y == w - 1:
        print(visit[cnt][x][y])
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue

        if visit[cnt][nx][ny] or arr[nx][ny] == 1:
            continue

        visit[cnt][nx][ny] = visit[cnt][x][y] + 1
        q.append((cnt, nx, ny))

    # 말 움직임이 불가능한 경우 다음으로 스킵
    if cnt == 0:
        continue

    for i in range(8):
        hnx = x + hx[i]
        hny = y + hy[i]

        if hnx < 0 or hnx >= h or hny < 0 or hny >= w:
            continue

        if visit[cnt-1][hnx][hny] or arr[hnx][hny] == 1:
            continue

        visit[cnt-1][hnx][hny] = visit[cnt][x][y] + 1
        q.append((cnt - 1, hnx, hny))
print(-1)

# 3차원 BFS문제
# 벽부수고 이동하기랑 비슷한 느낌