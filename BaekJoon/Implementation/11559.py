from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
puyo = [list(input()) for _ in range(12)]

# BFS로 4개이상이 연결된 블럭을 찾고, 그 부분은 "."으로 변경.
# 그리고 조건에 만족하는 블럭을 찾으면 True 반환. 아니면 False 반환.
def bfs(a, b, type):
    visit[a][b] = 1
    q = deque()
    q.append((a, b))
    block = [(a, b)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if not visit[nx][ny] and puyo[nx][ny] == type:
                visit[nx][ny] = 1
                q.append((nx, ny))
                block.append((nx, ny))
    if len(block) > 3:
        for x, y in block:
            puyo[x][y] = "."
        return 1
    return 0

# 빈 자리에 떨어지는 함수
# 각 열마다 행의 값들을 넣은 뒤, 아래서부터 채우는 방식 이용.
def block_down():
    col = [[] for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if puyo[j][i] != ".":
                col[i].append(puyo[j][i])
                puyo[j][i] = "."
    for i in range(6):
        j = 11
        while col[i]:
            puyo[j][i] = col[i].pop()
            j -= 1

chain = 0 # 총 연쇄 횟수
while True:
    visit = [[0] * 6 for _ in range(12)]
    flag = 0 # flag가 1이상이면 한 번은 블럭을 찾았으니 통과.
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != ".":
                flag += bfs(i, j, puyo[i][j])
    # 아무런 블럭을 못찾았으면 더이상 진행할 필요가 없음.
    if not flag:
        break
    chain += 1
    block_down()
    
print(chain)
