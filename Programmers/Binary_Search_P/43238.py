def solution(n, times):
    answer = 0
    
    start = 0
    end = n * max(times)
    while start <= end:
        mid = (start + end) // 2
        total = sum(mid // i for i in times) # 해당 시간에 몇명을 심사할 수 있는지 확인.
        
        if total >= n: # 목표값보다 많다 -> 시간이 널널하다.(시간을 좀 줄여보자.)
            end = mid - 1
        else: # 목표값보다 적다 -> 시간이 좀 부족하다(시간을 좀 늘려보자.)
            start = mid + 1
    answer = start
    return answer