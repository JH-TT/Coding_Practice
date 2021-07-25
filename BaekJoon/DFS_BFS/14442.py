from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0))
visit[0][0][0] = 1
while q:
    a, b, c = q.popleft()
    if a == n - 1 and b == m - 1:
        break
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        z = c
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if arr[x][y]: # 벽이면
            if z == k:
                continue
            z += 1 # k보다 작으면 벽을 부순다.
        if not visit[x][y][z]: # 방문하지 않았다면.
            visit[x][y][z] = visit[a][b][c] + 1 # 이전에 이동한 칸수에 1을 더해준다.
            q.append((x, y, z))
if max(visit[n - 1][m - 1]) == 0: # 전부 0이면 -1 출력.
    print(-1)
else: # 그렇지 않으면 0보다 큰 원소중에 최솟값을 출력.
    res = max(visit[n - 1][m - 1])
    for i in visit[n - 1][m - 1]:
        if i > 0:
            res = min(res, i)
    print(res)

# 여기 EscapeMaze랑 비슷한 문제. 다만 EscapeMaze는 벽을 한 번만 부수지만 여기는 최대 k개까지 가능.