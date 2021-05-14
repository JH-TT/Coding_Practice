import sys
import heapq
input = sys.stdin.readline

n = int(input())
a = []

res1 = 0
res2 = 0

for _ in range(n):
    heapq.heappush(a, int(input()))

m_arr = [] # 음수, 0을 저장할 공간.
p_arr = [] # 양수들만 저장할 공간.

for i in a:
    if i <= 0:
        heapq.heappush(m_arr, i)
    else:
        heapq.heappush(p_arr, -i) # 최소힙에서 양수 최댓값을 뽑으려면 부호를 반대로하고 뽑는다.


while len(m_arr) > 1:
    x1 = heapq.heappop(m_arr); y1 = heapq.heappop(m_arr)
    res1 += x1 * y1
if len(m_arr):
    res1 += m_arr[-1] # 나머지 하나는 더함.

# 양수부분은 최소힙때문에 부호를 반대로 해 놓음.
while len(p_arr) > 1:
    x2 = heapq.heappop(p_arr); y2 = heapq.heappop(p_arr)
    # 둘 중 하나라도 양수 1인 경우.
    if x2 == -1 or y2 == -1:
        res2 -= x2 + y2 # 음수기 때문에 빼준다.
        continue
    res2 += x2 * y2
if len(p_arr):
    res2 -= p_arr[-1] # 나머지 하나는 더함.

print(res1 + res2)