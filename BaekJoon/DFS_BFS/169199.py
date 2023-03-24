from collections import deque

def solution(board):
    answer = 0
    # 상하좌우 : 0123
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                start = [i, j]
    q = deque()
    visit = [[0] * len(board[0]) for _ in range(len(board))]
    q.append((0, start))
    while q:
        cnt, p = q.popleft()
        a, b = p
        if board[a][b] == "G":
            return cnt
        for i in range(4):
            if visit[a][b]:
                continue
            nex = move(a, b, i, board)
            q.append((cnt+1, nex))
        visit[a][b] = 1
    
    return -1

def move(x, y, t, b):
    if t == 0:
        while x > 0:
            if b[x-1][y] == "D":
                break
            x -= 1
    elif t == 1:
        while x < len(b)-1:
            if b[x+1][y] == "D":
                break
            x += 1
    elif t == 2:
        while y > 0:
            if b[x][y-1] == "D":
                break
            y -= 1
    else:
        while y < len(b[0])-1:
            if b[x][y+1] == "D":
                break
            y += 1
    return [x, y]