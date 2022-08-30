import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float('inf')
graph = [[0 if i == j else INF for i in range(n + 1)] for j in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1 , n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end =" ")
    print()

# 대충 문제보고 일반 플로이드 워셜이용하면 틀림.
# 문제에 조건을 잘 보고 풀도록