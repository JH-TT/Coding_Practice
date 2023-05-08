from collections import deque
import sys
input = sys.stdin.readline

def getConnection(x, y, k, t):
    con = []
    nt = (t+1) % 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visit[nx][ny] <= k: # 이미 k보다 이하로 벽을 부수고 왔으면 패스
            continue
        if arr[nx][ny] == "0": # 벽이 아니면 밤낮 상관없이 이동 가능
            con.append((nx, ny, k, nt))
        else:
            if k < K and t == 0: # 낮시간에 벽을 만나고 아직 더 부술 수 있다면 벽을 부수고 이동.
                con.append((nx, ny, k+1, 1))
    if t == 1: # 현재 밤이면 한 번 멈출 수 있다.(한 번 머물고 낮에 벽을 부수기위함)
        con.append((x, y, k, 0))
    return con

def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        cnt, x, y, k, t = q.popleft()
        if x == N-1 and y == M-1:
            print(cnt)
            return
        for nx, ny, nk, nt in getConnection(x, y, k, t):
            visit[nx][ny] = nk
            q.append((cnt+1, nx, ny, nk, nt))
    
    print(-1)

N, M, K = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visit = [[K+1 for _ in range(M)] for _ in range(N)] # visit[i][j] i, j 좌표까지 오는데 k개의 벽을 부수고 옴.
visit[0][0] = 0
bfs((1, 0, 0, 0, 0))