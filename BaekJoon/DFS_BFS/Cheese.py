from collections import deque
import copy

n, m = map(int, input().split())

cheese = []

result = []
melt = 0
count = 0

for _ in range(n):
    cheese.append(list(map(int, input().split())))

# 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):    
    q = deque()
    q.append((a, b))
    
    # 공기인 부분은 a로 지정.
    cheese[a][b] = "a"
    visit = [[0] * m for _ in range(n)]
    visit[a][b] = 1
    # q가 빌때까지
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            # 공기랑 접촉한 부분은 a로 바꿈.(녹아서 공기부분이 될거기 때문.)
            if cheese[x][y] == 1:
                cheese[x][y] = "a"
            # 0이고 방문했으면 그 좌표는 a로 바꾸고 방문처리후 q에 넣음.
            if cheese[x][y] == 0 and not visit[x][y]:
                cheese[x][y] = "a"
                visit[x][y] = 1
                q.append((x, y))

# 처음 남아있는 치즈구간.(한번에 전부 녹는 경우가 있으니 미리 저장)
for i in range(n):
    for j in range(m):
        if cheese[i][j] == 1:
            count += 1

# 치즈구간이 없어질때까지 반복.
while count > 0:
    result.append(count) # 치즈 구간개수를 결과값에 저장.
    count = 0 # 초기화

    # 너비우선탐색 시작.
    bfs(0, 0)
    # 남은 치즈구간개수 확인이랑, a인부분 다시 0으로 초기화.
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                count += 1
            elif cheese[i][j] == "a":
                cheese[i][j] = 0
    # 1시간 지남.
    melt += 1                

print(melt)
print(min(result))