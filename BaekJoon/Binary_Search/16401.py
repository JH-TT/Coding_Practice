import sys
input = sys.stdin.readline # 입력 빠르게 받기 위함.

m, n = map(int, input().split())

a = list(map(int, input().split()))

start = 1
end = max(a) + 1

while start <= end:
    mid = (start + end) // 2
    t = sum(x // mid for x in a)
    if t < m:
        end = mid - 1
    else:
        start = mid + 1

if end: # end가 양수면 그대로 출력
    print(end)
else: # 그 외에는 나눌 수 없다는 뜻이므로 0출력.
    print(0)