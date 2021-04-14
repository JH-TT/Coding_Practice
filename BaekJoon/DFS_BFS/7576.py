from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())

tomato = []

for _ in range(n):
    tomato.append(list(map(int, input().split())))

visit = [[0] * m for _ in range(n)]

cor = []

def bfs():
    q = deque()
    cnt = 0
    for a, b in  cor:
        visit[a][b] = 1
        q.append((a, b, 0)) # 좌표 a, b와 날짜인 0을 넣는다.
    while q:
        a, b, c = q.popleft()

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            
            if tomato[x][y] == 0 and not visit[x][y]:
                visit[x][y] = 1
                tomato[x][y] = 1
                cnt = c + 1 # 하루가 지남.
                q.append((x, y, c + 1))
    
    return cnt


# 1인 좌표들을 cor에 모아놓는다.
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            cor.append((i, j))

# bfs를 통해 결과값을 result에 넣는다.
result = bfs()

# 만약 0이있으면 result에 -1을, 아니면 그대로 출력.
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            result = -1

print(result)