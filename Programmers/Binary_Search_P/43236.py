def solution(distance, rocks, n):
    answer = 0
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    start = 0
    end = distance
    target_cnt = len(rocks) - n # 총 연결해야할 바위의 개수들
    
    while start <= end:
        mid = (start + end) // 2 # 기준이 되는 거리
        
        if check(mid, target_cnt, rocks):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    
    return answer

def check(d, m, rocks):
    cnt = 1
    cur = rocks[0]
    for next in rocks:
        if cur + d <= next:
            cnt += 1
            if cnt >= m:
                return True
            cur = next
    return False

# 마지막 distance를 밟는지 체크안하는 이유!
# 처음에는 마지막 골인 지점에 딱 들어가는지 확인을 해야하지 않나 생각했지만
# 만약에 distance를 넘어버리는 상황이 되면 마지막으로 밟은 돌을 없애면 된다고 판단하게 되었다.
# 그래서 마지막 돌을 없애는 판단으로 조건이 완료되면 거기서 거리를 조금씩 조절하면서 답에 가까워 지도록 설계한 것이다.