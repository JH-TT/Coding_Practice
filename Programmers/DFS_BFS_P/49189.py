from collections import deque

def solution(n, vertex):            
    answer = 0
    edge = [[] for _ in range(n+1)] # 간선정보
    visit = [0] * (n + 1) # 방문했는지 아닌지
    far = 0 # 가장 먼 거리
    for i in vertex:
        # *양방향*
        edge[i[0]].append(i[1])
        edge[i[1]].append(i[0])
    visit[1] = 1 # 1번 노드에서 시작
    q = deque()
    q.append([1, 0]) # 노드와 현재 거리 저장.
    dist = [0] * (n + 1) # 각 거리들
    
    while q:        
        node, cnt = q.popleft()
        far = max(far, cnt)
        
        for n in edge[node]:
            if not visit[n]: # 아직 방문하지 않은 노드면
                visit[n] = 1 # 방문처리 후 큐에 거리 + 1을 해주고 넣는다
                q.append([n, cnt + 1])
        
        dist[node] = cnt
    
    answer = dist.count(far) # 현재 가장 먼 거리인 노드 개수 구하기
    
    return answer