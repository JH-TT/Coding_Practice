import sys
from collections import deque
input = sys.stdin.readline

# 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
a = 1 # 넓이

result = [] # 넓이를 받을 리스트


# BFS
m, n, k = map(int, input().split())
area = [[0] * (n) for _ in range(m)]

for _ in range(k):
    # 왼쪽 아래 꼭짓점의 좌표, 오른쪽 위 꼭짓점의 x, y 좌표
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            area[i][j] = 1

def bfs(x, y):
    # 아까 정의한 전역변수 a를 가져온다. 0인 지역이니 면적은 1부터 시작.
    global a
    # 해당 노드 방문표시
    area[x][y] = 1
    # deque 라이브러리 사용
    q = deque()
    q.append((x, y))
    # 큐가 빌때까지 반복
    while q:
        x, y = q.popleft()
        for i in range(4): # 상하좌우 탐색
            xx = dx[i] + x
            yy = dy[i] + y
            # 해당범위에 있으면 수행
            if m > xx >= 0 and n > yy >= 0:
                if area[xx][yy] == 0:
                    area[xx][yy] = 1
                    q.append((xx, yy))
                    # 바로근처에 0인 칸을 찾았으니 면적 + 1
                    a += 1

count = 0
for i in range(m):
    for j in range(n):
        if area[i][j] == 0:
            count += 1
            bfs(i, j)
            result.append(a)
            a = 1  # 영역 넓이를 구했으면 다시 1로 초기화 시킨다.

result.sort()
print(count)
print(*result)