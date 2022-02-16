import heapq

T = int(input())

for _ in range(T):
    k = int(input())
    q = []
    arr = list(map(int, input().split()))
    total = 0
    for x in arr:
        heapq.heappush(q, x)
    while len(q) != 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        total += a + b
        heapq.heappush(q, a + b)

    print(total)

# 힙을 이용해서 가장 작은 2개를 꺼내서 합치고 다시 힙에 넣는 방식으로 한다.