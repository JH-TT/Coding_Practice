# 2805번과 거의 같은 문제. 단 이 문제는 시간이 2초가 주어짐. 그리고 나누기를 이용하는 것이라 mid가 0이 되는것을 조심하는 문제.
k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

start = 1
end = max(arr) + 1

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    total += sum([x // mid for x in arr])

    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)