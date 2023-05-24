import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [0] * 1000002

max_x = 0
for _ in range(n):
    g, x = map(int, input().split())
    dist[x] = g
    max_x = max(x, max_x)

# k의 범위가 x보다 넓기 때문에 이 조건문이 필요함.(이 부분때문에 시간날림)
if 2*k >= max_x:
    print(sum(dist))
    exit()
  
for i in range(max_x+1):
    dist[i] += dist[i-1]

res = 0
for i in range(2*k, max_x+1):
    res = max(res, dist[i] - dist[i-2*k-1])
print(res)

# 투 포인터
# 누적합