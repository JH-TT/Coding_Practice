# 나의 풀이
def solution(n, works):
    answer = 0
    
    if n >= sum(works):
        return 0
    
    m = len(works)
    total = sum(works)-n
    start = 0
    end = max(works)
    
    while start < end:
        mid = (start + end) // 2
        s = sum([min(x, mid) for x in works])
        if s < total:
            start = mid+1
        elif s >= total:
            end = mid
    
    works = sorted([min(x, start) for x in works], reverse = True)
    sub = sum(works) - total
    for i in range(sub):
        works[i] -= 1
    
    return sum(x ** 2 for x in works)
# 이진탐색을 이용해서 n의 작업량을 뺀 작업량의 평탄화를 구한다.
# 그 뒤에 목표 작업량보다 넘었으면 1씩 빼준다.

  
# 힙을 이용한 풀이
import heapq

def solution(n, works):
    answer = 0
    
    if n >= sum(works):
        return 0
    q = []
    for x in works:
        heapq.heappush(q, -x)
        
    while n:
        a = heapq.heappop(q)
        heapq.heappush(q, a+1)
        n -= 1
        
    while q:
        answer += (-heapq.heappop(q)) ** 2
    return answer

# 힙에 음수로 바꿔서 저장한다.
# 힙에서 최솟값을 꺼낸뒤, 1을 더하고 다시 힙에 넣는다(값이 음수라 1을 더해야 한다).
# 이렇게 n번 반복하면 평탄화가 될 것이고 각 원소에 제곱을 해서 합한다.