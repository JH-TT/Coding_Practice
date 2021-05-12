from collections import deque

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
target_s, target_x, target_y = map(int, input().split())
data = []

for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            data.append((a[i][j], 0, i, j)) # 바이러스의 데이터 입력.(바이러스 종류, 시작, 좌표)
data.sort() # 낮은 번호부터니까 오름차순 정렬.
q = deque(data) # 큐로 옮기기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs시작.
while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if a[nx][ny] == 0:
                a[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(a[target_x - 1][target_y - 1])