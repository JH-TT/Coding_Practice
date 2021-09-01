n, k = map(int, input().split())

tall = list(map(int, input().split()))
cost = [0] * (n - 1)
for i in range(n - 1):
    cost[i] = tall[i + 1] - tall[i]

cost.sort()    
print(sum(cost[:n - k]))

# cost부분까지는 구현했으나, 거기서 cost를 또 정렬해서 하는 건 몰랐었다.
# cost를 정렬하고 거기서 0번 인덱스부터 n - k - 1인덱스까지의 합을 구한다.