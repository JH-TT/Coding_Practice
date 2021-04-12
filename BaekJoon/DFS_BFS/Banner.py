from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input().rstrip())
maps = [list(map(int, input().rstrip())) for _ in range(n)] # sys를 import했다면 끝에 rstrip()을 해준다.
a = 0
result = []
visit = [[0] * n for _ in range(n)]

def bfs(a, b, c):
    q = deque()
    q.append((a, b))
    count = 1 # 같은동 아파트 개수.
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if maps[x][y] == 1 and not visit[x][y]:
                visit[x][y] = 1
                count += 1
                q.append((x, y))
    return count                

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and not visit[i][j]:
            visit[i][j] = 1
            house = bfs(i, j, a)
            if house:
                a += 1 # 아파트 단지
                result.append(house)

result.sort() # 오름차순으로 정렬.
print(a)
for i in result:
    print(i)