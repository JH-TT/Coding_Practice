from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C, T = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(R)]

m = []
for i in range(R):
    if space[i][0] == -1:
        m.append(i)


for _ in range(T):
    dust = deque()
    for i in range(R):
        for j in range(C):
            if space[i][j] > 0:
                dust.append([i, j, space[i][j]])

    while dust:
        x, y, d = dust.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if space[nx][ny] == -1:
                continue
        
            num = d // 5
            space[nx][ny] += num
            space[x][y] -= num

    # 위쪽
    for i in range(m[0] - 2, -1, -1):
        space[i + 1][0] = space[i][0]
    
    space[0] = space[0][1:] + [0]
    
    for i in range(1, m[0] + 1):
        space[i - 1][C - 1] = space[i][C - 1]
    
    space[m[0]] = [-1, 0] + space[m[0]][1:-1]

    # 아래쪽
    for j in range(m[1] + 2, R):
        space[j - 1][0] = space[j][0]

    space[R - 1] = space[R - 1][1:] + [0]
    
    for j in range(R - 2, m[1] - 1, -1):
        space[j + 1][C - 1] = space[j][C - 1]
    
    space[m[1]] = [-1, 0] + space[m[1]][1:-1]

for i in range(R):
    print(space[i])
    
ans = 0

for i in range(R):
    for j in range(C):
        if space[i][j] > 0:
            ans += space[i][j]
print(ans)

# 브루스포스 알고리즘. 주어진 조건대로 구현만 잘 하면 문제없이 통과할 수 있던 문제.
# 단 파이썬은 웬만해선 시간초과가 뜸. Pypy3로 출제함.