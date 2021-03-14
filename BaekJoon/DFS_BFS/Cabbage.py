# DFS
import sys
sys.setrecursionlimit(100000) # 재귀 최대 깊이 선언.

a = int(input())  # 테스트 케이스 개수
def dfs(x, y):
    # 범위를 벗어나면 바로 종료
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    # 현재노드를 아직 방문하지 않았다면
    if area[y][x] == 1:
        # 해당 노드 방문처리
        area[y][x] = 0
        # 상, 하, 좌, 우의 위치도 확인
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for _ in range(a):
    result = 0
    m, n, k = map(int, input().split()) # 가로, 세로, 배추개수
    area = [[0] * m for _ in range(n)] # 일단 전부 0으로 둠.
    for i in range(k):
        x, y = map(int, input().split())  # 좌표입력받기
        area[y][x] = 1 # 그 좌표는 1로 설정
    for i in range(m):
        for j in range(n):
            if dfs(i, j):  # True이면 result에 1을 더함.
                result += 1
    print(result)

# BFS (함수부분만 구현, 나머지는 거의 같음)
from collections import deque
# 이동할 4방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 해당노드는 방문표시
    area[x][y] = 0
    # 큐 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x, y))
    # 큐가 빌때까지 반복
    while q:
        x, y = q.popleft()
        for i in range(4): # 상하좌우 탐색
            xx = dx[i] + x
            yy = dy[i] + y
            # 해당범위에 있다면 수행
            if n > xx >= 0 and m > yy >= 0:
                if area[xx][yy] == 1:
                    area[xx][yy] = 0
                    q.append((xx, yy))