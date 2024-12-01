import heapq, sys
input = sys.stdin.readline

left = [] # 가장 큰 놈이 중간에 가까움
right = [] # 가장 작은 놈이 중간에 가까움
for _ in range(int(input())):
    n = int(input())
    if not left:
        heapq.heappush(left, -n)
        print(-left[0])
        continue
    if -left[0] < n:
        heapq.heappush(right, n)
    else:
        heapq.heappush(left, -n)

    # 2개 차이나면 개수를 맞춘다.
    if len(left) - len(right) == 2:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) - len(left) == 2:
        heapq.heappush(left, -heapq.heappop(right))

    # 이제 가운데를 출력한다
    if len(left) >= len(right):
        print(-left[0])
    else:
        print(right[0])

# 큐를 2개 이용해서 출력하는게 관건이었던 문제