n, m = map(int, input().split())

INF = float('inf')

arr = [[INF if i != j else 0 for i in range(n+1)] for j in range(n+1)] # 자기자신만 거리0 나머지는 INF

for _ in range(m):
    # 방향성이 없으므로 양쪽에 정보를 넣어준다.
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
  
# 플로이드 워셜 알고리즘 실행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# 각 총 거리와 친구번호를 같이 저장.
total = [[sum(i[1:]), idx+1] for idx, i in enumerate(arr[1:])]
total.sort() # 거리순, 친구번호순으로 정렬
print(total[0][1])


# 플로이드워셜 기본문제