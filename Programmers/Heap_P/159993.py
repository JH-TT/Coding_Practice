import heapq

def solution(maps):
    lever_min = 10001
    exit_min = 10001
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                s_x, s_y = i, j
            if maps[i][j] == "L":
                l_x, l_y = i, j
    # start -> lever
    q = []
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    heapq.heappush(q, (0, s_x, s_y))
    visit[s_x][s_y] == 1
    
    while q:
        cnt, x, y = heapq.heappop(q)
        
        if maps[x][y] == "L":
            lever_min = cnt
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == "X":
                continue
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                heapq.heappush(q, (cnt+1, nx, ny))
        
    
    # lever -> end
    q = []
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    heapq.heappush(q, (0, l_x, l_y))
    visit[l_x][l_y] = 1
    
    while q:
        cnt, x, y = heapq.heappop(q)
        
        if maps[x][y] == "E":
            exit_min = cnt
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == "X":
                continue
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                heapq.heappush(q, (cnt+1, nx, ny))

    print(lever_min)
    print(exit_min)
    
    return lever_min + exit_min if lever_min != 10001 and exit_min != 10001 else -1

# start -> lever -> end가 최소일 조건
# (a. start -> lever로 최소로 이동) + (b. lever -> end로 최소로 이동)
# 최소로 이동의 조건
# 겹치는 곳 없어야 한다. (visit 이용)
# -> a와 b는 서로 겹쳐서 이동해도 상관없지만 a, b 각각의 상황을 볼때 각자 겹쳐서 이동해선 안된다.

# 그래서 heap을 이용해서 cnt를 기준으로 오름차순으로 나오게 해서 이동시킨다.
# 만약 도착지에 오면 이동거리 업데이트하고 해당 케이스는 종료.

# 둘 중에 하나라도 이동거리가 10001이상이면 (최대 100X100) 탈출 불가능하니 -1을 리턴. 그게 아니면 더한값을 리턴.

# heap 관련 코드가 a상황 b상황 거의 같기 때문에 함수로 따로 만들어서 
# 파라미터를 추가해 각각의 상황으로 돌리면 코드가 더 깔금해질듯 하다.