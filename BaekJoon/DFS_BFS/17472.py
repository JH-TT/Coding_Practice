from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 섬의 개수 + 섬의 번호를 매긴다. 죄 -> 우, 상 -> 하 순.
def number_of_island(a):
    cnt = 0
    visit = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] > 0 and not visit[i][j]:
                a[i][j] = cnt+1
                cnt += bfs(i, j, a, visit, cnt + 1)
    return cnt, a # 섬의 개수와, 섬의 번호가 매겨진 리스트를 리턴한다.

def bfs(a, b, island_, visit, no):
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    while q:
        x, y = q.popleft()
      
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if island_[nx][ny] > 0:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    island_[nx][ny] = no
                    q.append([nx, ny])
    return 1 # 다 돌면 1을 리턴해서 섬의 개수를 측정한다.

# 직선으로 움직임. 리턴값은 다리 길이와 섬의 번호.
def move_straight(a, b, idx, land):
    cnt = 0
    while 1:
        a += dx[idx]
        b += dy[idx]
        if a < 0 or a >= n or b < 0 or b >= m:
            break
        if land[a][b] > 0:
            if cnt > 1:
                return cnt, land[a][b]
            break
        cnt += 1
    return 0, 0
        

# 섬과 섬을 잇는 모든 다리 탐색.
def bridges(island_):
    b = []
    for i in range(n):
        for j in range(m):
            if island_[i][j] == 0:
                continue
            for h in range(4):
                b_len, land_no = move_straight(i, j, h, island_)
                if land_no == 0:
                    continue
                from_to = [island_[i][j], land_no]
                from_to = sorted(from_to)
                a = [from_to, b_len]
                if a not in b:
                    b.append(a)
    return b

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
answer = 10**6
island = [list(map(int, input().split())) for _ in range(n)]
num_island, island = number_of_island(island)
bridge = bridges(island) # 다리 정보를 받는다.

# 다리를 고르는 모든 경우의 수
for brid in combinations(bridge, num_island-1):
    parent = [x for x in range(num_island+1)]
    bias = []
    cnt = 0
    for a, b in brid:
        bias.append((b, a[0], a[1]))
    bias.sort()
    for bia in bias:
        c, a, b = bia
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cnt += c   
    flag = True
    for i in range(2, num_island+1):
        if i == parent[i]:
            flag = False
            break
    if flag:
        answer = min(answer, cnt)
        
print(answer if answer != 10**6 else -1)

# 문제를 푼 방식
# 모든 섬을 잇는데 최소로 가질 다리 개수 -> 섬의 개수-1
# 섬을 잇는 모든 다리를 구하고, combination으로 섬의 개수 - 1개 만큼 뽑는 경우의 수를 구함.
# 그 경우의 수들을 가지고 다리를 만들고, 모든 섬이 이어질 경우 answer를 갱신한다.
# answer가 그대로면 섬을 못 잇는 것이므로 -1 출력, 아니면 answer의 값을 출력한다.
# 이때 모든 섬이 이어지는 판단은 크루스칼 알고리즘을 이용.
# 1번 노드를 제외한 다른 노드가 자기 자신을 가리키면 섬을 전부 잇지 못한것. -> line 104 ~ 110