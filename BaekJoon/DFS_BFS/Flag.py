# 기존 bfs개념에 4방향탐색에서 8방향탐색으로 바뀐거말곤 같음.
from collections import deque

# 8방향
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

m, n = map(int, input().split())

visit = [[0] * n for _ in range(m)]
flag = []
count = 0

for _ in range(m):
    flag.append(list(map(int, input().split())))

def bfs(a, b): 
    visit[a][b] = 1
    q = deque()
    q.append((a, b))

    while q:
        a, b = q.popleft()
        
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]

            if x < 0 or x >= m or y < 0 or y >= n:
                continue
            if flag[x][y] == 1:
                if not visit[x][y]:
                    flag[x][y] = 0
                    visit[x][y] = 1
                    q.append((x, y))

for i in range(m):
    for j in range(n):
        if flag[i][j] == 1 and not visit[i][j]:
            flag[i][j] = 0
            bfs(i, j)            
            count += 1


print(count)