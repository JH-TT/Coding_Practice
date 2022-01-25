from collections import deque

def solution(maps): 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]
    visit[0][0] = 1
    
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            
            if not visit[nx][ny] and maps[nx][ny] != 0:
                visit[nx][ny] = 1
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))    
    
    
    return maps[-1][-1] if visit[-1][-1] else -1