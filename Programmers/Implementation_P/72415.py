import heapq

def solution(board, r, c):
    global answer
    answer = 10**6

    dist = [[] for _ in range(7)]
    total_erase = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dist[board[i][j]].append([i, j])
                total_erase += 1
    dfs(dist, board, r, c, [], total_erase, 0, r, c)
    return answer

def dfs(dist, board, a, b, erase, total, key, r, c): # a, b : 현재 커서 좌표
    global answer

    if len(erase) == total:
        answer = min(answer, key)
        return 0

    for i in dist:
        if i == []:
            continue
        for j in range(2):
            if i[j] in erase:
                continue
            # 여기까지 오면 이동할 수 있는 좌표임 (r, c) -> (i[j][0], i[j][1]) 이때 키 조작 횟수
            sub = bfs(erase, board, [a, b], i[j])
            # 현재 카드에서 같은 카드로 이동
            sub += 1 # 카드 확인 엔터누르기
            sub += bfs(erase, board, i[j], i[(j+1)%2]) # 이동하는데 최소 조작 횟수
            sub += 1 # 이동 후 카드 확인 엔터
            dfs(dist, board, i[(j+1)%2][0], i[(j+1)%2][1], erase + i, total, key + sub, r, c)

def bfs(erase, board, cor, des):
    q = []
    if cor == des:
        return 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visit = [[[0, 0] for _ in range(4)] for _ in range(4)]
    visit[cor[0]][cor[1]] = [1, 1]
    heapq.heappush(q, (0, cor))
    while q:
        cnt, c = heapq.heappop(q) # flag : ctrl 누르고 있는지 아닌지
        x, y = c
        if c == des:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            ctrl_nx, ctrl_ny = move_ctrl(board, c, dx[i], dy[i], erase)
            if visit[nx][ny][0]:
                if visit[ctrl_nx][ctrl_ny][1]:
                    continue
                visit[ctrl_nx][ctrl_ny][1] = 1
                heapq.heappush(q, (cnt+1, [ctrl_nx, ctrl_ny]))
            else:
                visit[nx][ny][0] = 1
                heapq.heappush(q, (cnt+1, [nx, ny]))
                if visit[ctrl_nx][ctrl_ny][1]:
                    continue
                visit[ctrl_nx][ctrl_ny][1] = 1
                heapq.heappush(q, (cnt+1, [ctrl_nx, ctrl_ny]))

def move_ctrl(board, cor, dx, dy, erase):
    x, y = cor
    while True:
        x += dx
        y += dy
        if x < 0 or x >= 4 or y < 0 or y >= 4:
            return x-dx, y-dy
        if board[x][y] != 0 and ([x, y] not in erase):
            return x, y

