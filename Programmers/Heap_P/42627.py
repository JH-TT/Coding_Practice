import heapq

def solution(jobs):
    l = len(jobs)
    jobs.sort()
    
    t, answer, heap = 0, 0, []
    while jobs:
        a = 0
        for i in range(len(jobs)):
            if jobs[i][0] <= t:
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            else:
                jobs = jobs[i:]
                a = 1
                break
        if a == 0:
            jobs = []
        if heap:
            delay, start = heapq.heappop(heap)
            t += delay
            answer += t - start
        else:
            start, delay = jobs.pop(0)
            t = start + delay
            answer += delay
    while heap:
        delay, start = heapq.heappop(heap)
        t += delay
        answer += t - start
    
    
    return answer // l

# heap에 있는 요소들은 다른 작업이 진행중일때 요청이 온 작업들임.
# job은 요청이 오지않은 작업들임.
# 정확한 해설은 https://blog.naver.com/jjys9047/221731103669 참고.


# 다른 풀이.
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]))) # 걸리는 시간 기준으로 정렬함.
    q = []
    heapq.heappush(q, tasks.popleft()) # 첫번째 작업 q에 넣음
    current_time, total_response_time = 0, 0
    while len(q) > 0: # q가 빌 때 까지.
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur) # 현재 시간 + 걸리는 시간 or 작업 요청시간 + 걸리는 시간 중에 더 큰 값을 넣는다.
        total_response_time += current_time - arr # 그렇게 구한 현재시간에서 요청시간을 빼 주면, 요청시간부터 작업이 끝나는데 걸리는 시간이 된다.
        while len(tasks) > 0 and tasks[0][1] <= current_time: # 작업중에 요청이 들어오는 경우.
            heapq.heappush(q, tasks.popleft()) # 계속해서 넣어준다.
        if len(tasks) > 0 and len(q) == 0: # 당장 작업할거는 없는데, 아직 요청이 오지않은 남은 작업이 있는 경우 heap에 넣어준다.(하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다. <-- 이 조건에 해당하는 코드.)
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs) # 총 평균시간을 리턴한다.