from collections import deque

n = int(input())
k = int(input())
board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = "a"

l = int(input())
move = [0] * 10001

for _ in range(l):
    sec, d = input().split()
    move[int(sec)] = d

timer = 0

snake = deque([[1, 1]])
dx = [0, 1, 0, -1] # →, ↓, ←, ↑ 순서로 저장.
dy = [1, 0, -1, 0]
t = 0

i, j = 1, 1

while 1:
    timer += 1
    
    i += dx[t]
    j += dy[t]
    if i < 1 or i >= n+1 or j < 1 or j >= n+1:        
        break
        
    if [i, j] in snake:
        break
    # 사과가 없으면 몸 길이 그대로 옮긴다.
    if board[i][j] == 0:
        snake.popleft()            
    elif board[i][j] == "a":
        board[i][j] = 0        
    snake.append([i, j])

    # 방향 전환이 있는 경우
    if move[timer] == "D":
        t += 1
        t %= 4
    elif move[timer] == "L":
        if t == 0:
            t = 3
        else:
            t -= 1

print(timer)