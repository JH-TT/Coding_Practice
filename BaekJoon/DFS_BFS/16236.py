from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sea = [list(map(int, input().split())) for _ in range(n)]
shark = 2 # 초기 상어 크기.
t = 0 # 아기상어가 물고기를 잡아먹는 시간(초).

def bfs(a, b, d):
    global fish, visit # fish와 visit의 리스트를 가지고 옴.
    q = deque() # 큐 생성.
    visit[a][b] = 1 # 그 위치는 방문처리.
    q.append((a, b, d)) # q에 그 위치와 현재까지의 거리(걸린시간) 저장.
    while q: # q가 빌때까지 반복.
        x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visit[nx][ny] == 1:
                continue
            # 상어보다 더 큰 물고기면 방문처리만 함.
            if sea[nx][ny] > shark:
                visit[nx][ny] = 1
                continue
            # 그 외
            else:
                # 그 위치에 물고기가 있고, 크기가 아기상어보다 작으면 fish에 위차값과 걸리는 시간 저장.
                # 크기가 같거나 0이면 fish에 저장안하고 그냥 지나감.
                if 0 < sea[nx][ny] < shark:
                    fish.append((nx, ny, d + 1))
                visit[nx][ny] = 1
                q.append((nx, ny, d + 1))

c = shark
while 1:
    fish = [] # 아기상어보다 작은 모든 물고기의 위치.
    visit = [[0] * n for _ in range(n)] # 지나친 곳인지 체크.
    # 상어위치 탐색.
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sea[i][j] = 0
                bfs(i, j, 0)
    if len(fish) == 0: # 더이상 아기상어가 물고기를 먹을 수 없을 때
        break
    else:
        fish.sort(key=lambda x:(x[2], x[0], x[1])) # 걸리는시간, 행, 열 순으로 정렬.
    X, Y, D = fish[0] # 가장 적합한 물고기
    sea[X][Y] = 9 # 아기상어는 그 물고기가 있던 위치로 감.
    t += D # 걸리는 시간 더함.
    c -= 1
    # 상어의 크기만큼 물고기를 먹었으면 아기상어의 크기가 1증가하고, 다시 c에 저장.
    if c == 0:
        shark += 1
        c = shark
print(t)