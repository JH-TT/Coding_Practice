from collections import deque

node = int(input()) # 컴퓨터의 개수
n = int(input()) # 컴퓨터 쌍의 수

com = [[] for _ in range(node + 1)]
visit = [False for _ in range(node + 1)]

for _ in range(n):
    i, j = map(int, input().split())
    com[i].append(j)
    com[j].append(i)

def bfs(com, start, visit):
    result = 0

    q = deque([start])
    visit[start] = True

    while q:
        v = q.popleft() # 노드를 꺼냄.
        for i in com[v]: # 그 노드와 연결된것들 확인.
            if not visit[i]: # 아직 안본 노드가 있으면
                q.append(i) # 그 노드를 넣음
                visit[i] = True # 방문처리
                result += 1 # 바이러스 + 1
    return result              


print(bfs(com, 1, visit))  