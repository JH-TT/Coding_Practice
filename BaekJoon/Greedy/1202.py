import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

j = [list(map(int, input().split())) for _ in range(n)]
backpack = [int(input()) for _ in range(k)]
j.sort()
backpack.sort()

total = 0
candi = []

for b in backpack:
    while j and b >= j[0][0]:
        heapq.heappush(candi, -j[0][1])
        heapq.heappop(j)
      
    print(candi)
    if candi:
        total += heapq.heappop(candi)
    elif not j:
        break

print(-total)

# 현재 가방안에 들어갈 수 있는 후보들을 넣는다.
# 그 중에 가장 비싼 보석을 뺀다.
# 나머지 후보는 그대로 다음 가방에 이어서 간다.
# 반복.
# 이런식으로 푸는건 생각했는데, 구현을 어떤식으로 할 지 생각하느라 좀 걸렸던 문제..... 넘 아쉽