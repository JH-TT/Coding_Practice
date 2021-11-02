import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
poly = [list(map(int, input().split())) for _ in range(n)]

# dfs로 "ㅗ"모양 제외하고 나머지 모양을 탐색한다.
def bfs(a, b):
    q = deque()
    # 좌표, 블럭 수, 현재 값, 지나온 좌표 정보들을 넣는다.
    q.append([a, b, 1, poly[a][b], [[a, b]]])
    max_res = 0 
    while q:
        x, y, cnt, score, cor = q.popleft()
        # 블럭이 4개가 되면 다음꺼 보러감.
        if cnt == 4:
            max_res = max(max_res, score)
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 지나갔는지 체크
            if [nx, ny] not in cor:
                q.append([nx, ny, cnt+1, score+poly[nx][ny], cor + [[nx, ny]]])
    return max_res

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, bfs(i, j))

# "ㅗ" 모양 탐색
for i in range(n):
    for j in range(m):
        try:
            # "ㅜ" 만 되는 경우
            if i == 0:
                s = poly[i][j] + poly[i+1][j] + poly[i][j-1] + poly[i][j+1]
                ans = max(ans, s)
            # "ㅏ" 만 되는 경우
            elif j == 0:
                s = poly[i][j] + poly[i+1][j] + poly[i-1][j] + poly[i][j+1]
                ans = max(ans, s)
            # "ㅗ" 만 되는 경우
            elif i == n - 1:
                s = poly[i][j] + poly[i-1][j] + poly[i][j-1] + poly[i][j+1]
                ans = max(ans, s)
            # "ㅓ" 만 되는 경우
            elif j == m - 1:
                s = poly[i][j] + poly[i+1][j] + poly[i][j-1] + poly[i-1][j]
            # "ㅗ, ㅏ, ㅜ, ㅓ 다 되는 경우"
            else:
                s = poly[i][j] + poly[i+1][j] + poly[i][j-1] + poly[i][j+1] + poly[i-1][j]
                mini = min(poly[i+1][j], poly[i][j-1], poly[i][j+1], poly[i-1][j])
                ans = max(ans, s - mini)
        # 구석처럼 "ㅗ"모양이 나오지 않는 경우는 예외처리함
        except:
            continue

print(ans)