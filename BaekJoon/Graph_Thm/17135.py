from itertools import combinations
from collections import deque
import copy

dx = [0, -1, 0]
dy = [-1, 0, 1]

n, m, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
enemy = sum(sum(x) for x in arr)

res = 0
for combi in combinations(list(range(m)), 3):
    arr2 = copy.deepcopy(arr)
    kills = 0 # 총 잡은 적의 수
    enemy2 = enemy # 총 적의 수
    while enemy2:
        kill = set() # 활 맞은 적의 좌표
        for archer in combi:
            q = deque()
            visit = [[0 for _ in range(m)] for _ in range(len(arr2))]
            q.append((len(arr2)-1, archer, 1)) # n번째 행부터 시작하니 1칸 이동한셈.
            visit[-1][archer] = 1
            while q:
                x, y, cnt = q.popleft()
                # 거리 초과
                if cnt > d:
                    continue
                # 적 발견
                if arr2[x][y] == 1:
                    kill.add((x, y))
                    break
                for i in range(3):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= len(arr2) or ny < 0 or ny >= m:
                        continue
                    if visit[nx][ny] == 1:
                        continue
                    visit[nx][ny] = 1
                    q.append((nx, ny, cnt+1))
        for k in kill:
            arr2[k[0]][k[1]] = 0
            kills += 1
            enemy2 -= 1
        enemy2 -= sum(arr2.pop())
    res = max(res, kills)
print(res)

# BFS로 풀긴했는데 그 외에 브루트포스 등 다른 알고리즘도 있어서 그래프 이론에 넣음