import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now, track):
    if len(track) == 5:
        print(1)
        exit() # 더 이상 볼 필요가 없으니 강제 종료시킨다.

    for nxt in graph[now]:
        if nxt not in track:
            dfs(nxt, track + [nxt])

for i in range(n):
    dfs(i, [i])
print(0)

# 복잡한 문제인줄알고 식겁했지만, 단순 깊이가 5가 되면 종료되는 문제.