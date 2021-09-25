n = int(input())

cost = [0] + list(map(int, input().split()))

for i in range(2, n + 1):
    for j in range(1, i//2 + 1):
        cost[i] = min(cost[i], cost[j] + cost[i - j]) # i개 사는 가격과 j개 가격 + i - j개 가격 중에 최솟값으로 둔다.
        
print(cost[n])