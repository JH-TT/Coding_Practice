from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cor = [] # 바이러스 위치
res = [] # 결과값

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a):
    t = 0
    visited = [[0] * n for _ in range(n)]
    arr2 = copy.deepcopy(arr)
    q = deque()
    for i in a:
        visited[i[0]][i[1]] = 1
        q.append(i + [0])
    while q:
        a, b, t2 = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if not visited[x][y]:
                # 빈 공간이면 시간을 늘려서 확산시킴
                if arr2[x][y] == 0:
                    t = max(t, t2+1)
                    arr2[x][y] = t2 + 1
                    visited[x][y] = 1
                    q.append([x, y, t2 + 1])
                # 비활성화 바이러스면 활성화되지만, t를 업데이트 하진 않는다.(구석에 비활성화면 어차피 바이러스이므로 시간잴 필요 없음)
                elif arr2[x][y] == 2:
                    visited[x][y] = 1
                    q.append([x, y, t2 + 1])
    # 바이러스가 다 퍼지지 못하면 -1리턴.
    for i in range(n):
        for j in range(n):
            if not arr2[i][j]:
                return -1
    return t

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            cor.append([i, j])     
# 바이러스가 있을 수 있는 경우의 수 모두 저장.            
cor2 = combinations(cor, m)
# bfs를 돌려서 바이러스가 모두 퍼진 경우에만 res에 저장.
for i in cor2:
    tt = bfs(i)
    if tt >= 0:
        res.append(tt)
# res가 비었다는 말은 바이러스를 모두 전파시키지 못하는 경우 이므로 -1 출력. 그 외에는 최솟값 출력.
print(min(res) if res else -1)