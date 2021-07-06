from bisect import bisect_left
import sys
input = sys.stdin.readline
m = float('inf')

t = int(input())

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