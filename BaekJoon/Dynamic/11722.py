from bisect import bisect_left

n = int(input())

seq = list(map(int, input().split()))
cnt = [1] * n

for i in range(1, n):
    for j in range(i):
        if seq[i] < seq[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)
print(max(cnt))

# 각 숫자들 기준 왼쪽에 자신보다 큰 숫자가 있으면, 그 큰 숫자의 cnt값에서 1 더한것과 자신의 cnt 값중에 큰 것을 자신의 cnt값으로 지정한다.