import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

line = []
visit = [0 for _ in range(n + 1)]
line_visit = [0 for _ in range(l)]
g = [[] for _ in range(n + 1)]
for i in range(l):
    *nodes, _ = map(int, input().split())
    # v역은 i노선에서 j번째에 속한다.
    for j in nodes:
        g[j].append(i)
    line.append(nodes)

s, e = map(int, input().split())

# 주체를 잘 잡아야 한다.
q = deque()
q.append(s)
visit[s] = 1
while q:
    now = q.popleft()

    if now == e:
        print(visit)
        if now == s:
            print(0)
            exit()
        print(visit[e] - 2)
        exit()

    for i in g[now]:
        if line_visit[i]: continue
        line_visit[i] = 1
        for j in line[i]:
            if visit[j]: continue
            visit[j] = visit[now] + 1
            q.append(j)
print(-1)

# 이 문제는 어떤걸 기준으로 bfs를 돌리냐이다.
# 일단 역이랑 노선을 방문체크를 하긴 하지만, 주 된 q에 값을 넣냐 마냐는 노선의 방문을 기준으로 한다.
# 만약 가지 않은 노선이면 환승횟수를 1을 증가시키고 해당 노선에 있는 방문하지 않았던 역을 전부 넣는 방식을 한다.