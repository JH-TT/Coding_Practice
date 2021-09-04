T = int(input())
for _ in range(T):    
    n, m, k = map(int, input().split())
    house = [0] + list(map(int, input().split()))
    if n == m:
        if sum(house) < k:
            print(1)
        else:
            print(0)
        continue        
    house += house[1:m]
    n += m
    for i in range(1, n):
        house[i] = house[i] + house[i - 1]
    print(house)
    cnt = 0
    for i in range(1, n - m + 1):
        if house[i+m-1] - house[i-1] < k:
            cnt += 1
    print(cnt)
# 이 문제는 구간합 빠르게 계산하는 방법으로 하면 시간초과가 안난다.
# 구간합을 빨리 계산하기위해선 접두사 합(Prefix_Sum)을 계산해 배열P에 저장한다.(첫번째는 0으로 시작.)
# 구간 [L, R]에서의 합을 구하려면 P[R] - P[L-1]을 해주면 구간합이 나오게 된다.