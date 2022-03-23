from collections import deque

def solution(board):
    INF = int(1e9)
    answer = INF
    n = len(board)
    # 3차원 리스트로 상하좌우로 갈 모든 경우를 탐색한다
    visit = [[[INF for _ in range(n)] for _ in range(n)] for i in range(4)]
    # 하오위왼
    # 여기부턴 bfs
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = deque()
    for i in range(4):
        visit[i][0][0] = 0
    if board[0][1] == 0:
        q.append([0, 1, 100, 1])
        visit[1][0][1] = 100
    if board[1][0] == 0:
        q.append([1, 0, 100, 0])
        visit[0][1][0] = 100
        
    while q:
        a, b, c, d = q.popleft()
        
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            
            if na < 0 or na >= n or nb < 0 or nb >= n:
                continue
            
            if d != i:
                nc = c + 600
            else:
                nc = c + 100
            if board[na][nb] == 0:
                if nc < visit[i][na][nb]:
                    q.append([na, nb, nc, i])
                    visit[i][na][nb] = nc
    answer = min(visit[z][-1][-1] for z in range(4)) # 그래서 상하좌우 4가지경우중 최솟값을 answer로 업데이트

    return answer