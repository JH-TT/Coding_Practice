n, c = map(int, input().split())

a = []
for _ in range(n):
    a.append(int(input()))
a.sort()

start = 0 # 가장 작은 gap
end = a[-1] - a[0] # 가장 큰 gap
result = 0
while start <= end:
    mid = (start + end) // 2
    value = a[0]
    cnt = 1
    for i in range(1, n):
        if a[i] >= value + mid: # gap을 만족시키는 안테나면 cnt에 1을 더한다.
            value = a[i]
            cnt += 1
    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)

# 이 문제는 막상 바로 떠오르기는 쉽지 않았던 문제.
# 안테나끼리의 gap을 이용해 이진탐색을 하는 방법.