import heapq

def solution(k, score):
    answer = []
    q = []
    
    for i in score:
        if len(q) < k:
            heapq.heappush(q, i)
            answer.append(q[0])
            continue
        if q[0] < i:
            heapq.heappop(q)
            heapq.heappush(q, i)
        answer.append(q[0])
    
    return answer


# 더 간단한 풀이
import heapq

def solution(k, score):
    answer = []
    q = []
    
    for i in score:
        heapq.heappush(q, i)
        
        if len(q) > k:
            heapq.heappop(q)
        answer.append(q[0])
    
    return answer

# 이 문제의 핵심
# k개를 넘기지 않게 저장하되 오른차순으로 있어야 한다.
# 그냥 heapq을 이용해서 계속 넣다가 k개를 넘기면 최솟값을 빼버리는 전략을 이용하면 됨