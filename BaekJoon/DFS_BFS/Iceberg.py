from collections import deque
import copy
import sys
input = sys.stdin.readline

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
ice = []

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit = [[0] * m for i in range(n)]
    visit[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and ice_3[x][y] != 0:
                ice_3[x][y] = 0
                visit[x][y] = 1
                q.append([x, y])

def check(i, j):
    cnt = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < n and 0 <= y < m and ice_2[x][y] == 0:
            cnt += 1
    return cnt

# 다 녹았는데도 분리가 안되었는지 확인.
def Melt():
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0:
                return False
    return True

# ice 입력받기
for i in range(n):
    ice.append(list(map(int, input().split())))

result = 1

while True:
    if Melt():
        print(0)
        break
    ice_2 = copy.deepcopy(ice)
    for i in range(n):
        for j in range(m):
            if ice_2[i][j] != 0:
                a = ice[i][j] - check(i, j)
                ice[i][j] = a if a >= 0 else 0

    ice_3 = copy.deepcopy(ice)
    cnt = 0

    for i in range(n):
        for j in range(m):
            if ice_3[i][j] != 0:
                ice_3[i][j] = 0
                bfs(i, j)
                cnt += 1

    if cnt > 1:
        print(result)
        break
    result += 1