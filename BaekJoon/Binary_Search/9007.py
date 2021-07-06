from bisect import bisect_left
import sys
input = sys.stdin.readline
m = float('inf')

t = int(input())
# 1
for _ in range(t):
    k, n = map(int, input().split())
    a1 = []
    a2 = []
    res = m
    arr = [list(map(int, input().split())) for _ in range(4)]
    for i in range(n):
        for j in range(n):
            a1.append(arr[0][i] + arr[1][j]) # 위 2줄의 모든 경우의 수
            a2.append(arr[2][i] + arr[3][j]) # 아래 2줄의 모든 경우의 수
    a1.sort() # 정렬
    a2.sort() 
    
    # bisect를 이용해서 이분탐색 시작.
    for i in a1:
        idx = bisect_left(a2, k - i) # k에서 a1의 요소를 뺀 나머지와 거의 수가 비슷한 위치
        # 지금 탐색하는 수의 차이가 더 작으면 res를 새로 갱신.
        if idx < n*n and abs(k - i - a2[idx]) < abs(k - res):
            res = i + a2[idx]
        # 차이가 같으면 둘 중 최솟값을 res로 갱신
        elif idx < n*n and abs(k - i - a2[idx]) == abs(k - res):
            res = min(res, i + a2[idx])
        # 바로 왼쪽 인덱스도 탐색한다.
        if abs(k - i - a2[idx - 1]) < abs(k - res):
            res = i + a2[idx - 1]
        elif abs(k - i - a2[idx - 1]) == abs(k - res):
            res = min(res, i + a2[idx - 1])
    print(res)

# 2
import sys
input = sys.stdin.readline
m = float('inf')

t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    a1 = []
    a2 = []
    res = []
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(n):
            a1.append(arr1[i] + arr2[j])

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            a2.append(arr1[i] + arr2[j])
    a1.sort()
    a2.sort(reverse = True)

    res = gap = m
    f = s = 0
    len = n * n
    while f < len and s < len:
        t = a1[f] + a2[s]

        if abs(res - k) > abs(k - t):
            res = t
        elif abs(res - k) == abs(k - t):
            res = min(res, t)
        if t >= k:
            s += 1
        else:
            f += 1
    print(res)
# 걸린 시간은 2번째가 더 빨랐다.
# 아마도 탐색부분에서 차이가 난듯.
# 1은 a1의 모든 요소를 뒤지지만, 2는 투포인터 개념으로 적절하게 하나씩 보니까 더 빠른거 같다.