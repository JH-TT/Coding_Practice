from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edge = [[] for _ in range(n+1)]
visit = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
  
q = deque()
cnt = 0
# 모든 노드를 방문했는지 확인
for i in range(1, n+1):
    # 만약 처음 방문하는 노드면 바로 bfs실행.
    if not visit[i]:
        q.append(i)            
        while q:
            node = q.popleft()
            for i in edge[node]:
                if not visit[i]:
                    visit[i] = 1
                    q.append(i)
        cnt += 1
print(cnt)