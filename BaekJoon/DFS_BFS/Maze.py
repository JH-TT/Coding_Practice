from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 너비 우선탐색.
def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if arr[nx][ny] == 0:
                continue

            if arr[nx][ny] == 1:
                
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1 # 길이 있으면 그 전 숫자에 1을 더한 값을 넣음.(몇번째 칸인지 체크)
                    q.append((nx, ny))

          return arr[n - 1][m - 1]
                        

    return arr[n - 1][m - 1]

print(bfs(0, 0))