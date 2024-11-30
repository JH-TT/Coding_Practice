import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    global res
    visit[x] = True
    cycle.append(x)
    nxt = team[x]

    if visit[nxt]:
        if nxt in cycle:
            res += cycle[cycle.index(nxt):]
        return
    else:
        dfs(nxt)


for _ in range(int(input())):
    n = int(input())
    team = [0] + list(map(int, input().split()))
    visit = [True] + [False] * n
    res = []

    for i in range(1, n + 1):
        if not visit[i]:
            cycle = []
            dfs(i)

    print(n - len(res))

# dfs를 돌리면서 아까 지났던 노드로 다시 오면 그 노드부터 끝까지 사이클로 보면서 확인한다.