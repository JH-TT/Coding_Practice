import sys
input = sys.stdin.readline

def dfs(node, type):
    if visit[node][type]:
        return
    visit[node][type] = 1
    for i in edge[node][type]:
        dfs(i, type)
    

n = int(input())
m = int(input())

edge = [[[], []] for _ in range(n+1)]

for _ in range(m):
    big, small = map(int, input().split())
    edge[big][1].append(small)
    edge[small][0].append(big)

for i in range(1, n+1):
    visit = [[0, 0] for _ in range(n+1)]
    dfs(i, 0)
    dfs(i, 1)
    res = 0
    for i in range(1, n+1):
        if sum(visit[i]) == 0:
            res += 1
    print(res)


# 플로이드 워셜로 푼 방식
import sys
input = sys.stdin.readline
    
n = int(input())
m = int(input())
INF = 10**5
arr = [[INF] * n for _ in range(n)]

for i in range(n):
    arr[i][i] = 1

for _ in range(m):
    big, small = map(int, input().split())
    arr[big-1][small-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(n):
    res = 0
    for j in range(n):
        if arr[i][j] == INF and arr[j][i] == INF:
            res += 1
    print(res)

# 내가 푼 방식이 더 빠르긴 했다.