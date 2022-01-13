import sys
input = sys.stdin.readline

n = int(input())

edge = [list(map(int, input().split())) for _ in range(n)]
edges = [[1] * n for _ in range(n)]

# 입력은 이미 플로이드워셜이 적용된 상태로 넘어온다.
# 다이렉트로 가는 길이랑 경유해서 가는길이 같으면 다이렉트길을 없앤다.
# 만약 다이렉트로 가는 길이 더 크면 잘못된 길이므로 -1을 출력한다.
res = 0
for k in range(n):
    for i in range(n):
        for j in range(n):                     
            if i == j or j == k or i == k:
                continue            
            if edge[i][j] == edge[i][k] + edge[k][j]:
                edges[i][j] = 0
            elif edge[i][j] > edge[i][k] + edge[k][j]:                
                print(-1)
                exit()

for i in range(n):
    for j in range(i, n):
        if edges[i][j]:
            res += edge[i][j]

print(res)