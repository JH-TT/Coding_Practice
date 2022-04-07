# 이 문제의 핵심
# 고둘라와 상근이의 위치를 같이 저장하는것

import heapq

# 상근이가 이동하는 동안 고둘라가 이동하는 함수
def move_godula(d, p):
    while p != len(godula)-1:
        if pos_godula[godula[p]][godula[p+1]] > d:
            return d, p
        d -= pos_godula[godula[p]][godula[p+1]]
        p += 1
    return d, p

INF = int(1e9)

n, m = map(int, input().split())
a, b, k, g = map(int, input().split())

godula = list(map(int, input().split()))
road = [[] for _ in range(n+1)]
pos_godula = [[0 for _ in range(n+1)] for _ in range(n+1)]

distance = [INF] * (n + 1)
visit = [0] * (n + 1)

for _ in range(m):
    u, v, l = map(int, input().split())
    road[u].append((v, l))
    road[v].append((u, l))
    pos_godula[u][v] = l
    pos_godula[v][u] = l

pos = 0
end = godula[-1]
k, pos = move_godula(k, pos) # 초반 k분 동안 고둘라만 이동
q = []
heapq.heappush(q, [(0, a), (k, pos)]) # 상근이의 위치와 거리, 고둘라의 위치와 거리
distance[a] = 0

while q:
    sang, god = heapq.heappop(q)
    # 지금 거리가 더 크면 스킵
    if distance[sang[1]] < sang[0]:
        continue
      
    for i in road[sang[1]]:  
        go = [] # 고둘라의 현재위치, 다음위치 저장할 리스트
        if god[1] != len(godula) - 1: # 아직 마지막이 아닌 경우에 리스트에 저장
            go = [godula[god[1]], godula[god[1]+1]]        
        sa = [sang[1], i[0]] # 상근이의 정보
        go.sort()
        sa.sort()
        if godula[god[1]] != end:
            if go == sa: # 고둘라가 현재 상근이가 가려는 도로를 달리고 있다면
                cost = sang[0] + i[1] + (pos_godula[godula[god[1]]][godula[god[1]+1]] - god[0]) # 고둘라가 도로를 빠져나가는 시간까지 합쳐준다.
                k, pos = move_godula(i[1], god[1]+1)
            else: # 그 외에는 그냥 상근이가 이동하는 시간만 저장.
                cost = sang[0] + i[1]
                k, pos = move_godula(i[1] + god[0], god[1])
        else:
            cost = sang[0] + i[1]
            k, pos = move_godula(i[1] + god[0], god[1])
          
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, [(cost, i[0]), (k, pos)])

print(distance[b])