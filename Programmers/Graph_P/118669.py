import heapq

def solution(n, paths, gates, summits):
    summits.sort() # intensity가 같으면 산봉우리 번호가 작은걸 우선으로 두기 때문에 미리 정렬한다.
    graph = [[] for _ in range(n+1)]
  
    q = []  
    for i in paths:
        a, b, c = i
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    visit = [float('inf') for _ in range(n + 1)]
    
    for i in gates:
        visit[i] = 0
        for j in graph[i]:
            heapq.heappush(q, (j[1], j[0]))
    
    while q:
        cost, node = heapq.heappop(q)
        
        if visit[node] <= cost:
            continue
        visit[node] = cost
        
        if node in summits:
            continue
        
        for i in graph[node]:
            if visit[i[0]] <= i[1]:
                continue
            heapq.heappush(q, (max(cost, i[1]), i[0]))
            
    answer = [0, float('inf')]
    for i in summits:
        if visit[i] < answer[1]:
            answer = [i, visit[i]]
    
    return answer

# 다익스트라로 푼 문제.
# ps. 첨엔 다익스트라로 될까 의심만 했는데, 다익이 맞았음... dfs로 하려니 시간초과뜨고 참..... 다익이 편하긴 해