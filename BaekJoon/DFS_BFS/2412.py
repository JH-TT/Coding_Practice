from collections import deque
import sys

input = sys.stdin.readline
n, T = map(int, input().split())

cor = set() # set을 이용하면 좀 더 빠르게 처리 가능
for _ in range(n):
    x, y = map(int, input().split())
    cor.add((x, y))

# 이동 범위
dx = [-2, -1, 0, 1, 2]
dy = [-2, -1, 0, 1, 2]

q = deque()
q.append([0, 0, 0])

while q:
    x, y, cnt = q.popleft()
    if y == T: # 목표지점에 도착시 결과값 출력
        print(cnt)
        exit(0)    
    for i in range(5):
        for j in range(5):
            nx = x + dx[i]
            ny = y + dy[j]
            if (nx, ny) in cor: # 범위 안에 갈 수 있는 홈이 있으면
                q.append([nx, ny, cnt + 1]) # 그 쪽으로 이동
                cor.remove((nx, ny)) # 좌표값은 삭제
print(-1) # 끝까지 못 간다면 -1 출력