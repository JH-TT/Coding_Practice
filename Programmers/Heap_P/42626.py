import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2) # 가장 덜 매운 값 + 2번째로 덜 매운 값 * 2를 넣어준다.
        answer += 1
    if scoville[0] < K:
        return -1
    
    return answer
# 여기서 왜 heapify를 써야 통과되는지 모르겠다.
# heapify는 가장 작은값을 0번째 인덱스에 위치시키도록 하는것.