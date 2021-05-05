n = int(input())

a = list(map(int, input().split()))

start = 0
end = n - 1

result = 0
while start <= end:
    mid = (start + end) // 2
    if a[mid] == mid: # 고정점이면 mid 출력.
        result = mid
        break
    elif a[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1

if result:
    print(result)
else: # 고정점이 아니면 -1 출력
    print(-1)