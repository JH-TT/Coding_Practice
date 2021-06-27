n = int(input())
k = int(input())
s = list(map(int, input().split()))
s.sort()

dist = [s[i + 1] - s[i] for i in range(n - 1)]
dist.sort()

# 1. 센서보다 집중국이 더 많으면 각 센서에 배치해도되니 0이된다.
# 2. 그 외에는 각 센서끼리의 거리를 구하고 거기서 k-1개 만큼의 가장 긴 거리를 뺴준다.
if n < k:
    print(0)
else:
    cnt = 0
    while cnt < k - 1:
        dist.pop()
        cnt += 1
    print(sum(dist))