INF = 16

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
dist = [[INF for j in range(n + 1)] for i in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    dist[a][b] = min(c, dist[a][b])
    dist[b][a] = min(c, dist[b][a])

# 플로이드 워셜 알고리즘 적용
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

res = 0
# 하나씩 확인
# i번째에 있다고 가정
for i in range(1, n + 1):
    total = items[i]
    for j in range(1, n + 1):
        if i == j: continue

        if dist[i][j] <= m:
            total += items[j]
    res = max(res, total)

print(res)

# 플로이드 워셜 알고리즘으로 충분히 풀리는 문제
# 플로이드 워셜을 구현할때 주의해야할 점.
#    중간지점은 항상 제일 바깥 for loop에 있어야 함!
#    플로이드 워셜 원리가 점진적인 변화인데 k가 가장 안쪽 for loop에 있게되면 바로바로 정보들이 갱신되기 때문에 최신 거리값을 사용하지 못하게 됨!