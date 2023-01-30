from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n, m = len(maps), len(maps[0])
    
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]
    answer = []
    
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and maps[i][j] != "X":
                visit[i][j] = 1
                q = deque()
                q.append((i, j))
                total = int(maps[i][j])

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if maps[nx][ny] == "X":
                            continue
                        if not visit[nx][ny]:
                            visit[nx][ny] = 1
                            total += int(maps[nx][ny])
                            q.append((nx, ny))
                answer.append(total)
    
    return sorted(answer) if answer else [-1]
# 간단한 BFS, DFS 기본 문제