import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

def dfs(x, y):
    if visit[x][y] != 0:
        return visit[x][y]
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if arr[nx][ny] > arr[x][y]:
            visit[x][y] = max(visit[x][y], dfs(nx, ny) + 1)

    return visit[x][y]

res = 0
for i in range(n):
    for j in range(n):
        visit[i][j] = dfs(i, j)

for i in range(n):
    res = max(res, max(visit[i]))

print(res)

# 일단 dfs를 돌아서 끝까지 간 다음. 거기서 1씩 증가시킨다.
# 즉 14 9
#    12 11 이라면
# 9에서 dfs를 돌면 11 12를 거처서 14까지 가게되고 14는 더이상 움직일 수 없으니 1로설정 12는 2 11은 3 마지막으로 9에는 4로 저장.
# 이 방식을 반복한다.
# def + dp 문제였다.