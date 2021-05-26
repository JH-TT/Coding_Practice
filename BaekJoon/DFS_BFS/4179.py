from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]
visit_J = [[0] * C for _ in range(R)]
visit_F = [[0] * C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 불 먼저 확산 시키고나서 지훈이를 옮긴다.
def bfs():
    t = 1
    global j, f
    while j: # j가 빌 때 까지.
        f2 = deque()
        while f:
            a, b = f.popleft()
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                if na < 0 or na >= R or nb < 0 or nb >= C or maze[na][nb] == "#":
                    continue
                if not visit_F[na][nb]:
                    maze[na][nb] = "F"
                    visit_F[na][nb] = 1
                    f2.append((na, nb))
        f = f2 # 일단 한 텀에 한번씩 움직이니 f2큐를 따로 만들고 저장시킨 후 while문을 나오면 다시 f에 넣어준다.
        j2 = deque()
        while j:
            x, y = j.popleft()
            if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                return t
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if maze[nx][ny] == "F" or maze[nx][ny] == "#":
                    continue
                if maze[nx][ny] == "." and not visit_J[nx][ny]:
                    maze[nx][ny] == "J"
                    visit_J[nx][ny] = 1
                    j2.append((nx, ny))
        j = j2
        if not j: # 더이상 움직일 공간이 없을 때.
            break
        
        t += 1

j = deque()
f = deque()
for i in range(R):
    for k in range(C):
        if maze[i][k] == "J":
            j.append((i, k))
            visit_J[i][k] = 1
        elif maze[i][k] == "F":
            f.append((i, k))
            visit_F[i][k] = 1

res = bfs()
print(res if res != None else "IMPOSSIBLE")