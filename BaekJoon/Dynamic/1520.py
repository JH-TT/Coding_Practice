import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())
a = [list(map(int ,input().split())) for _ in range(M)]
t = [[-1] * N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y): 
    if x == M - 1 and y == N - 1:
        return 1
    if t[x][y] != -1:
        return t[x][y] # 이미 지났던 곳이면 그 인덱스의 값을 리턴한다.
    t[x][y] = 0 # 처음오면 0부터 시작.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if a[nx][ny] < a[x][y]: # 다음 높이가 더 낮으면 재귀시작.
            t[x][y] += dfs(nx, ny)

    return t[x][y]
print(dfs(0, 0))