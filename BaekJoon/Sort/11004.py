n, k = map(int, input().split())
print(sorted(list(map(int, input().split())))[k-1])

# 2초라 그런지 그냥 sorted함수로 풀렸다...
# 당연히 시간초과 뜰 줄 알고 heap쓴 나는...

# heap쓴 코드
import heapq

n, k = map(int, input().split())
a = []
b = list(map(int, input().split()))
for i in range(n):
    heapq.heappush(a, b[i])
c = 0
while k > 0:
    c = heapq.heappop(a)
    k -= 1
print(c)