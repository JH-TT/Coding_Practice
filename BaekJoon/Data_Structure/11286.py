import heapq, sys
input = sys.stdin.readline

q = []

for _ in range(int(input())):
    num = int(input())
    if num != 0:
        heapq.heappush(q, [abs(num), num])
    else:
        print(heapq.heappop(q)[1] if q else 0)


# 힙에 절댓값, 원래값 으로 저장.
# 그러면 절댓값 -> 원래값 순서로 정렬하기때문에 문제에 맞게 정렬됨.
# 그다음엔 0이면 출력