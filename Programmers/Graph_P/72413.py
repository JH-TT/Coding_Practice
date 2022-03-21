# 크루스칼 알고리즘 이용
import heapq

def solution(n, s, a, b, fares):
    d = [[10**9 for _ in range(n+1)] for _ in range(n+1)] 
    for i in range(n+1):
        d[i][i] = 0
    for x, y, z in fares:
        d[x][y] = z
        d[y][x] = z
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    min_ = 10**10
    for i in range(1, n+1):
        min_ = min(min_, d[s][i] + d[i][a] + d[i][b])
    
    return min_

# 다익스트라 이용
import heapq

def solution(n, s, a, b, fares):
    def dijkstra(start, end, distance):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]                
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))    

        return distance[end]

    answer = 10**10
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    for A, B, C in fares:
        graph[A].append([B, C])
        graph[B].append([A, C])

    for i in range(1, n+1):        
        a_fee = dijkstra(i, a, [INF] * (n + 1))
        b_fee = dijkstra(i, b, [INF] * (n + 1))
        c_fee = dijkstra(s, i, [INF] * (n + 1))        
        answer = min(answer, a_fee + b_fee + c_fee)  

    return answer
# 다익스트라 코드부분
# 각 노드에서 a까지 최단거리 + b까지 최단거리 + 시작지점에서 그 노드까지 최단거리를 각 노드마다 구해서 그 중에 최소를 출력.