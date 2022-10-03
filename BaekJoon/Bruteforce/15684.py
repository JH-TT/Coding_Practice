# 내 풀이
import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(s, level, g):
    q = deque()
    q.append([level, s])
    while q:
        lev, cur = q.popleft()
        if lev > h:
            if cur == s:
                return True
            else:
                return False
        if g[cur][lev] != 0:
            q.append([lev+1, g[cur][lev]])
        else:
            q.append([lev+1, cur])

n, m, h = map(int, input().split())
graph = [[0 for _ in range(h+1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b][a] = b+1
    graph[b+1][a] = b

valid_case = []
for i in range(1, n):
    for j in range(1, h+1):
        if graph[i][j] == 0 and graph[i+1][j] == 0 and graph[i-1][j] != i:
            valid_case.append((j, i))
# 사라디 추가 X
flag = True
for i in range(1, n+1):
    if not bfs(i, 1, graph):
        flag = False
        break
if flag:
    print(0)
else:
    # 사다리 추가
    g = copy.deepcopy(graph)
    for i in range(1, min(4, len(valid_case)+1)):
        if (m + i) % 2 != 0:
            continue
        combi = list(combinations(valid_case, i))
        for case in combi:
            flag1 = True
            for c in case:
                if g[c[1]][c[0]] != 0 or g[c[1]+1][c[0]] != 0:
                    flag1 = False
                    break
                g[c[1]][c[0]] = c[1] + 1
                g[c[1]+1][c[0]] = c[1]
            if not flag1:
                g = copy.deepcopy(graph)
                continue
            flag2 = True
            for j in range(1, n):
                if not bfs(j, 1, g):
                    flag2 = False
                    break
            if flag2:
                print(i)
                exit()
            for c in case:
                g[c[1]][c[0]] = 0
                g[c[1]+1][c[0]] = 0
                
    print(-1)
# 조합을 이용해서 그냥 모든 경우를 구하고 사다리가 잘 놓아졌는지 확인까지 해야해서 느린 풀이법이다.


# 빠른 코드
N, M, H = map(int, input().split())
if M == 0:
    print(0)
    exit(0)

ladder = [[0] * N for _ in range(H)]
#print(ladder)

for idx in range(M):
    x, y = list(map(int, input().split()))
    ladder[x - 1][y - 1] = 1
# for idx in range(H):
#     print(ladder[idx])

# 조건에 맞게 잘 가는지 확인
def check():
    for i in range(N): #세로
        k = i
        for j in range(H): #가로
            if ladder[j][k] == 1: #가로 오른쪽
                k += 1
            elif k > 0 and ladder[j][k - 1] == 1:
                k -= 1
        if k != i:
            return False
    return True

# (x, y) 좌표, 사다리 개수
def dfs(x, y, cnt):
    global ans
    # 맞게된 사다리면 ans 업데이트
    if check():
        ans = min(ans, cnt)
        #return
    # 3개가 넘을거같으면 리턴
    elif cnt == 3 or ans <= cnt:
        return
    else:
        # 같은 가로선이면 미리 구해놓은 세로선으로 이동. 그 외에는 0부터 탐색.
        for i in range(x, H): #가로선
            if i == x:
                k = y
            else:
                k = 0
            for j in range(k, N - 1): #세로선
                if ladder[i][j] == 0 and ladder[i][j + 1] == 0:
                    if j > 0 and ladder[i][j - 1] != 0:
                        continue
                    ladder[i][j] = 1
                    dfs(i, j + 2, cnt + 1)
                    ladder[i][j] = 0

#print('start')
#N 세로, M 가로, 추가 H
ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)