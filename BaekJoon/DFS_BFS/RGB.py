from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
RGB = []
R = 0 # R의 구간 개수
G = 0 # G의 구간 개수
B = 0 # B의 구간 개수
RnG = 0 # R또는 G의 구간 개수(R과G를 같은색으로 봄)
for _ in range(n):
    RGB.append(list(input()))

def bfs(a, b, color):
    visit = [[0] * n for _ in range(n)]

    q = deque()
    q.append((a, b))
    visit[a][b] = 1 # 해당 부분 방문처리

    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if RGB[x][y] != color:
                continue
            if RGB[x][y] == color: # 찾는 색이면 서 방문처리 안됐으면 실행.
                if not visit[x][y]:
                    if color == 'B':
                        RGB[x][y] = 'W' # B는 W로 수정.
                    elif color == 'R' or color == 'G':
                        RGB[x][y] = "K" # 정록생맥꺼를 따지기위해 R과G는 K로 수정.
                    else:
                        RGB[x][y] = "1" # 그 외에는 1
                    visit[x][y] = 1
                    q.append((x, y))

for i in range(n): # 일반인 부분
    for j in range(n):
        if RGB[i][j] == 'R':
            RGB[i][j] = 'K'
            bfs(i, j, 'R')
            R += 1
        elif RGB[i][j] == 'G':
            RGB[i][j] = "K"
            bfs(i, j, 'G')
            G += 1
        elif RGB[i][j] == 'B':
            RGB[i][j] = "W"
            bfs(i, j, 'B')
            B += 1

for i in range(n): # 정록색맹 부분
    for j in range(n):
        if RGB[i][j] == "K":
            RGB[i][j] = "1"
            bfs(i, j, 'K')
            RnG += 1

print(R + G + B, RnG + B)