def solution(t, p):
    answer = 0
    n = len(p)
    for i in range(len(t)-n+1):
        # 보통 논리식이 먼저 진행되기 때문에 해당 조건이 맞으면 1, 아니면 0을 리턴한다.
        # 그래서 해당 조건이 맞을때 마다 1씩 증가하게 된다.
        answer += int(t[i:i+n]) <= int(p)
        
    return answer