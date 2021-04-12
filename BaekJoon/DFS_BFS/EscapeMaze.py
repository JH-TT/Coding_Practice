from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

Maze = []

for i in range(n):
    Maze.append(list(map(int, input().split()))) # 미로생성

def bfs(a, b):
    visit = [[[-1, -1] for _ in range(m)] for _ in range(n)] # 왼쪽 -1은 벽을 한 번도 부수지 않고 올때, 오른쪽은 한번이라도 벽을 부수고 올 때.

    q = deque()
    q.append((a, b, 0))
    visit[a][b][0] = 0 # 0칸부터 시작.
    while q:
        a, b, c = q.popleft()
        if a == Ex-1 and b == Ey-1:
            return visit[a][b][c]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            z = c

            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if Maze[x][y]:
                if z: # 벽을 한번이라도 부쉈으면 다른좌표로 이동.
                    continue
                else: # 아니면 벽을 부순다.
                    z = 1
            if visit[x][y][z] == -1: # 아직 온 적 없는 곳이면 이전칸수에 1을 더한 값을 저장.
                visit[x][y][z] = visit[a][b][c] + 1
                q.append((x, y, z))
    return -1


print(bfs(Hx-1, Hy-1))