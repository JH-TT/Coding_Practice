import sys
from collections import deque
from itertools import permutations, combinations
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, c, d, visit):
    visit[a][b] = 1
    q = deque()
    q.append((a, b, 0))

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if room[nx][ny] == "x":
                continue
            
            if not visit[nx][ny]:
                if nx == c and ny == d:
                    return cnt + 1
                visit[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
    return -1
    

while 1:
    res = 99999999999    
    w, h = map(int, input().split())
    dist = [[[[-1] * 20 for _ in range(20)] for _ in range(20)] for _ in range(20)] # dist[nx][ny][x][y] := (nx, ny) -> (x, y) 까지 최소거리
    
    if w == 0 and h == 0:
        break

    room = [list(input()) for _ in range(h)]
    dirty = []

    for i in range(h):
        for j in range(w):
            if room[i][j] == "o":              
                robot_w = j
                robot_h = i
            elif room[i][j] == "*":
                dirty.append([i, j])
                
    for i in combinations([[robot_h, robot_w]] + dirty, 2): # 각 두 쓰레기끼리의 거리를 구해놓는다.
        visit = [[0] * w for _ in range(h)]        
        start_h = i[0][0]
        start_w = i[0][1]
        des_h = i[1][0]
        des_w = i[1][1]
        Cnt = bfs(start_h, start_w, des_h, des_w, visit)
        if Cnt == -1:
            break
        dist[start_h][start_w][des_h][des_w] = Cnt
        dist[des_h][des_w][start_h][start_w] = Cnt
        
    if Cnt == -1:
        print(-1)
        continue
    
    for i in permutations(dirty, len(dirty)): # 모든 거리를 탐색해서 최솟값을 계속 업데이트 해준다.
        i = [[robot_h, robot_w]] + list(i)
        move = 0
        for j in range(len(i) - 1):
            start_h = i[j][0]
            start_w = i[j][1]
            des_h = i[j + 1][0]
            des_w = i[j + 1][1]
            move += dist[start_h][start_w][des_h][des_w]
            
        res = min(res, move)
    print(res)

# Pypy3로 통과한 문제