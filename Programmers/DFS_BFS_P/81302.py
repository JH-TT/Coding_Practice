from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(places):
    answer = []
    
    def bfs(a, b, visit):
        q = deque()
        q.append((a, b, 0))
        visit[a][b] = 1
        while q:
            x, y, cnt = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if visit[nx][ny]:
                    continue
                  
                if place[nx][ny] == "O" and cnt < 2: # 거리가 아직 2이내고 뚫린길이면 간다.
                    visit[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))
                    
                if place[nx][ny] == "P" and cnt < 2: # 현재 1칸 이내움직였으면 다음이 P라는 소리이므로 바로 0을 리턴한다.
                    return 0
        return 1
    
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P": # 현재 P자리면 bfs실행
                    visit = [[0, 0, 0, 0, 0] for _ in range(5)]                    
                    flag = bfs(i, j, visit)
            if flag: # flag가 1이면 이미 거리두기가 안되는것이므로 바로 빠져나온다
                break
        answer.append(flag)
    
    return answer