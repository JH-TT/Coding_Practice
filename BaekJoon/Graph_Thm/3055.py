from collections import deque

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]
visit=[[0] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for i in range(r):
    for j in range(c):
        if maze[i][j] == "S":
            q.appendleft((i, j))
        elif maze[i][j] == "*":
            q.append((i, j))
        elif maze[i][j] == "D":
            r_x = i
            r_y = j

flag = False

while q:
    if flag:
        break
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if maze[x][y] == "*": # 물인경우
            if maze[nx][ny] == "." or maze[nx][ny] == "S":
                maze[nx][ny] = "*"
                q.append((nx, ny))
        elif maze[x][y] == "S": # 고슴도치인 경우
            if maze[nx][ny] == ".":
                maze[nx][ny] = "S"
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
            elif maze[nx][ny] == "D":
                visit[nx][ny] =  visit[x][y] + 1
                flag= True
print(visit[r_x][r_y] if visit[r_x][r_y] else "KAKTUS")

# 이건 참고한 코드. 내가 작성한 코드에서 문제점은
# 1. 고슴도치가 먼저 움직였어야 했다. 그런데 나는 물부터 움직임.(가장 중요했음)
# 2. 나는 물의 visit도 따로 처리했는데, 굳이 그럴필요 없었다.(maze의 값으로만 판단가능했기 때문.)
# 쉬운문젠데....이런건 실수를 줄이도록 해야겠다.