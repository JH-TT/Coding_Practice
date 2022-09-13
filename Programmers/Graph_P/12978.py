import heapq

def solution(N, road, K):
    INF = float('inf')
    distance = [INF] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    q = []
    heapq.heappush(q, [0, 1])
    distance[1] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        
        for i in graph[cur]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return sum([1 if i <= K else 0 for i in distance])


# 그냥 길이 여러개 들어올 수 있는 거 빼곤 다익스트라 기본문제. 사실 두 노드 사이에 여러 길이 와도 다익스트라 성격상 의미 없음