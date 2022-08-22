from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 공기체크
def checkair(a, b):
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[a][b] = 1
    cheese[a][b] = 'a'
    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
              
            if cheese[nx][ny] == 0 or cheese[nx][ny] == 'a':
                if visit[nx][ny]:
                    continue
                visit[nx][ny] = 1
                cheese[nx][ny] = 'a'
                q.append([nx, ny])

# 체크한 치즈 제거
def removecheese():
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 'c':
                cheese[i][j] = 'a'

# 모든 치즈가 없어졌는지 확인
def checkcheese():
    for i in cheese:
        if 1 in i:
            return False
    return True
  
''' 확인용 코드 : 치즈 출력하기
def printcheese():
    for i in cheese:
        print(*i)
    print()
'''

# 조건에 맞는 치즈 찾기
def findcheese():
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if cheese[i][j] != 1:
                continue
            cnt = 0
            for h in range(4):
                ni = i + dx[h]
                nj = j + dy[h]
                if cheese[ni][nj] == 'a':
                    cnt += 1
            if cnt >= 2:
                cheese[i][j] = 'c'

n, m = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(n)]
days = 0
checkair(0, 0)

while not checkcheese():
    findcheese()
    removecheese()
    checkair(0, 0)
    days += 1

print(days)