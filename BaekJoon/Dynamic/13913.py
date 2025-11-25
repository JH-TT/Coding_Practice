from collections import deque

def dfs(n):
    if parent[n] == n:
        res.append(n)
        return
    res.append(n)

    dfs(parent[n])

n, k = map(int, input().split())

INF = float('inf')

visit = [False] * 200001
parent = [-1] * 200001
visit[n] = True
parent[n] = n

q = deque()
q.append(n)

while q:
    now = q.popleft()

    if now == k:
        break

    for i in [-1, 1, now]:
        nxt = now + i

        if nxt < 0 or nxt > 200000:
            continue

        if visit[nxt]:
            continue

        visit[nxt] = True
        parent[nxt] = now
        q.append(nxt)

res = []
# dfs(k)

# 재귀는 터질 가능성이 있으므로 반복문으로 처리해보자
cur = k
while True:
    res.append(cur)
    if parent[cur] == cur:
        break
    cur = parent[cur]
# ============= 이렇게 하면 재귀깊이가 터질 위험도 없다.
print(len(res) - 1)
res.reverse()
print(*res)