from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

total = M * N * H

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dh = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, -1, 1, 0, 0]

tomato = []
ripe = 0
empty = 0

q = deque()
for h in range(H):
    row = []
    for x in range(N):
        l = list(map(int, input().split()))
        for y in range(len(l)):
            t = l[y]
            if t == 1:
                ripe += 1
                q.append((h, x, y))
            if t == -1:
                empty += 1
        row.append(l)
    tomato.append(row)

if ripe + empty == total:
    print(0)
else:
    time = 1 # 일차
    while True:
        q2 = deque()
        while q:
            h, x, y = q.popleft()

            for i in range(6):
                nh = h + dh[i]
                nx = x + dx[i]
                ny = y + dy[i]

                if nh < 0 or nh >= H or nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                if tomato[nh][nx][ny] == 1 or tomato[nh][nx][ny] == -1:
                    continue

                tomato[nh][nx][ny] = 1
                ripe += 1
                q2.append((nh, nx, ny))
        # 하루가 지난 뒤
        if ripe + empty == total:
            print(time)
            break
        # 안익은 토마토가 있지만 위치상 익을 수 없으면 종료
        if not q2:
            print(-1)
            break
        while q2:
            q.append(q2.popleft())
        time += 1
        
# 3차원으로 늘어난것 뿐이지 사실상 BFS 기본문제 수준