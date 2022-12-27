from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
ind = [0] * (n + 1)
res = [0] * (n + 1)
build = [0] * (n + 1)

for i in range(1, n+1):
    a, *c, _ = map(int, input().split())
    build[i] = a
    for j in c:
        graph[j].append(i)
        ind[i] += 1
q = deque()
for i in range(1, n+1):
    if ind[i] == 0:
        q.append(i) # 현재 건물과 지난 시간.
while q:
    node = q.popleft()
    res[node] += build[node] # res[node]는 지금 건물을 짓기 위한 사전 건물이 다 건설되는 시간이 저장돼 있다. 현재 건물을 지을 수 있는 상황이니 걸린 시간을 더해준다.
    for next in graph[node]:
        res[next] = max(res[next], res[node]) # 다음 건물은 사전건물이 전부 완성돼야지 건설할 수 있다. 즉 그말은 사전건물들중 가장 오래걸리는 건물이 기준이 된다.
        ind[next] -= 1
        # 다음 건물을 지을 수 있는 상황이 되면 q에 넣어준다.
        if ind[next] == 0:
            q.append(next)
for i in res[1:]:
    print(i)

# 기본 위상정렬 + DP

# 12-27일 다시 품.(2번만에 통과!)
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
ind = [0] * (n + 1)
t = [0] * (n + 1)
answer = [0] * (n + 1)
for i in range(1, n+1):
    cost, *a, _ = map(int, input().split())
    for j in a:
        ind[i] += 1
        graph[j].append(i)
    t[i] = cost

q = deque()
for i in range(1, n+1):
    if ind[i] == 0:
        q.append([t[i], i])
while q:
    time, node = q.popleft()
    answer[node] = time
    for next in graph[node]:
        ind[next] -= 1
        answer[next] = max(answer[next], time)
        if ind[next] == 0:
            q.append([answer[next] + t[next], next])

print(*answer[1:], sep="\n")