from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
house = [] # 집 위치들
chicken = [] # 치킨집 위치들
dist = [] # 각 치킨집 거리

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i + 1, j + 1))
        elif arr[i][j] == 2:
            chicken.append((i + 1, j + 1))

c_chicken = combinations(chicken, m) # m개 고르는 총 경우의 수.
for x in c_chicken:    
    t = 0
    for y in house:
        d = 2 * (n + 1) # 한 집과 한 치킨집 거리의 최댓값이 이 수를 넘을 수 없다.
        for z in x:
            d = min(d, abs(z[0] - y[0]) + abs(z[1] - y[1])) # 계속 현재 집과 여러 치킨집의 거리를 계산해서 d와 둘 중에 더 작은 값을 d로 둔다.
        t += d # for문을 빠져나오면 d는 한 집에서 치킨집까지 가장 가까운 거리가 되고 이것을 t에 누적시킨다.
    dist.append(t) # 거리를 담는 리스트에 t넣음
print(min(dist)) # 전부 계산한 거리중에 최솟값을 출력.

# 브루트포스 알고리즘이라 딱히 어려운 점은 없던 문제.