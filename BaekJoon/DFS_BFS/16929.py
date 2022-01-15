import sys
input = sys.stdin.readline

def dfs(a, b, cnt):
    if a < 0 or a >= n or b < 0 or b >= m:
        return

    visit[a][b] = cnt

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue        
        if cor[nx][ny] == cor[a][b] and not visit[nx][ny]:    
            dfs(nx, ny, cnt + 1)
    

n, m = map(int, input().split())


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cor = [list(input()) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            dfs(i, j, 1)

for i in range(n):
    for j in range(m):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if cor[ni][nj] == cor[i][j] and abs(visit[ni][nj] - visit[i][j]) >= 3:
                print("Yes")
                exit()
print("No") 

# 풀이방법.
# 1. dfs로 같은 값끼리 각 위치까지 몇번 움직여야 가는지 구해놓는다.
# 2. 같은 값끼리 움직인 횟수의 차가 3이상인지 확인하고 있으면 Yes
# 전부 확인했는데 없으면 No를 출력한다.