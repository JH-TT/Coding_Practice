import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

result = 0
while start <= end:
    mid = (start + end) // 2
    # list comprehension 이용. for문보단 더 빠름.
    total = sum([i - mid if i > mid else 0 for i in tree])
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)    