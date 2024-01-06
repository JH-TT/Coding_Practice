from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

INF = 10**6

n = int(input())
maze = [input() for _ in range(n)]
visit = [[INF for _ in range(n)] for _ in range(n)]

visit[0][0] = 0
q = deque()
q.append((0, 0, 0)) # 좌표, 몇개의 색을 바꿨는지

while q:
    x, y, cnt = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visit[nx][ny] <= cnt:
            continue
        visit[nx][ny] = cnt
        # 넘어갈 곳이 검은방이면 색 변경하고 넘어간다.
        if maze[nx][ny] == '0':
            q.append((nx, ny, cnt + 1))
        else: # 흰색이면 그대로 이동
            q.append((nx, ny, cnt))        

print(visit[-1][-1])

# 일단 n의 범위가 50밖에 되지 않았고
# 부순 횟수가 가장 적은 경우를 구하는 문제였기 때문에
# visit을 부순 횟수를 저장하도록 하고 해당 위치로 오는데에 벽을 더 적게 부쉈을 경우에만 업데이트 하도록 한다.
# 그러면 O(n^2) 정도밖에 되지 않아서 충분히 통과한다.