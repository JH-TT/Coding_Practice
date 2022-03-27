from collections import deque

def solution(rectangle, cX, cY, itemX, itemY):
    answer = int(1e9)
    field = [[0 for _ in range(101)] for _ in range(101)]
    
    # 가장자리 1로 채우기
    for r in rectangle:
        min_x = r[0] * 2
        max_x = r[2] * 2
        min_y = r[1] * 2
        max_y = r[3] * 2
        for y in range(min_y, max_y+1):
            if y == min_y or max_y:
                for x in range(min_x, max_x+1):
                    field[y][x] = 1
            else:
                field[y][min_x] = 1
                field[y][max_x] = 1
    
    # 전부 겹친 후 내부 1없애기
    for r in rectangle:
        min_x = r[0] * 2
        max_x = r[2] * 2
        min_y = r[1] * 2
        max_y = r[3] * 2
        for y in range(min_y+1, max_y):
            for x in range(min_x+1, max_x):
                if field[y][x] == 1:
                    field[y][x] = 0
                    
    # bfs 돌리기
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[0 for _ in range(101)] for _ in range(101)]
    visit[cY*2][cX*2] = 1
    q = deque()
    q.append([cY*2, cX*2, 0])
    
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                continue  
            if nx == itemX*2 and ny == itemY*2:
                answer = min(answer, (cnt+1) // 2)
                break
            if not visit[ny][nx] and field[ny][nx] == 1:
                visit[ny][nx] = 1
                q.append([ny, nx, cnt+1])
    
    return answer

# 범위를 2배로 늘려서 한 이유
# ㄷ자 모양 같은 경우 바로 위로 넘어가는 경우가 생기기 때문에 2배로 늘려서 세세하게 가도록 설정했음