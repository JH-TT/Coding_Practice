import heapq

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    dist = [-1] * (n + 1)
    q = [(destination, 0)]
    dist[destination] = 0
    while q:
        now = q.pop(0)
        for next in graph[now[0]]:
            if dist[next] == -1:
                dist[next] = now[1]+1
                q.append((next, now[1]+1))
                
    return [dist[s] for s in sources]

# 다익스트라 비스무리하게 풀면 되는 문제였다. 
# 여기는 이동 비용이 1로 통일이라서 따로 cost를 저장할 필요가 없었다. 
# 그말은 dist값이 -1 아니면 그게 최솟값이 되는것이고 -1로 돼있으면 아직 가지않은 노드가 된다. (방문처리를 따로할 필요가 없다.)