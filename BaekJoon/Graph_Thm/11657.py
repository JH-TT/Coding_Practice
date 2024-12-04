import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            now = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]

            if dist[now] != INF and dist[now] + cost < dist[nxt]:
                dist[nxt] = dist[now] + cost

                if i == n - 1:
                    return True
    return False

flag = bf(1)

if flag:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])

# 벨만 포드 알고리즘 문제
# 1. 주어진 간선을 먼저 전부 확인한다.
# 2. 그 간선들을 가지고 1번을 n - 1번 반복한다.
# 3. 그 뒤에 한 번 더 1번을 진행하다가 또 거리가 업데이트되면 음수 사이클이 존재하다는 의미가 된다.