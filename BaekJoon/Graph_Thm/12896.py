# 정답 코드. (스크루지 민호)
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    distance = [0] * (n + 1)
    visit[node] = 1
    q = deque([node])

    while q:
        nod = q.popleft()
        for i in graph[nod]:
            if visit[i] == -1:
                visit[i] = 1
                distance[i] = max(distance[nod] + 1, distance[i])
                q.append(i)
    return distance.index(max(distance)), max(distance)

visit = [-1] * (n + 1)
node1, dist = bfs(1) # 아무노드 (여기선 1번 노드)에서 가장 먼 노드를 구한다.

visit = [-1] * (n + 1)
node2, dist = bfs(node1) # 그 노드에서 가장 먼 길이를 구한다.

print((1 + dist) // 2) # 그 길이의 절반을 출력한다.

# 아무노드를 골라서 가장 멀리있는 노드를 찾는다.
# 그 노드에서 가장 긴 거리를 구하고 그 거리의 절반을 출력해 준다.
# 이 문제는 백준 1167번 트리의 지름을 보는것이 좋다.
# https://merona99.tistory.com/280
# https://moonsbeen.tistory.com/366


# 실패했던 코드
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node, cnt, visit):
    visit[node] = 1
    q = deque()
    q.append([node, cnt])

    while q:
        nod, max_dist = q.popleft()

        for i in graph[nod]:
            if visit[i] == -1:
                visit[i] = 1
                # 아무래도 이 부분이 시간을 많이 잡아먹었나 보다. 정답과 비교해 보면 딱히 큰 차이가 없지만 계속 시간초과가 뜨는걸 보면 sum함수떄문인것 같다.
                if sum(visit) == n - 1:
                    return i, max_dist + 1
                
                q.append([i, max_dist + 1])    

# 이 곳도 원래는 for문으로 각 노드의 최대 길이를 구해주고 거기서 최솟값을 출력했었다
# 그런데 그러기엔 너무 오래걸려서 시간초과가 났고, 힌트를 찾아보니 트리의 지름과 관련있었다.
visit = [-1] * (n + 1)
node, dist = bfs(1, 0, visit) 

visit = [-1] * (n + 1)
node, dist = bfs(node, 0, visit) 

print((1 + dist) // 2) 

# 총평 : 메모이제이션을 자주쓰자!