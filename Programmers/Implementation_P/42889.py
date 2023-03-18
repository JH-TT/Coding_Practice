def solution(N, stages):
    state = [0] * (N+2) # 스테이지에 있는 사람의 수
    answer = [[0, i] for i in range(len(state))]
    for i in stages:
        state[i] += 1
        
    n = len(stages)
    for i in range(1, len(state)-1):
        try:
            answer[i][0] = state[i] / (n-state[i-1])
            n -= state[i-1]
        except:
            break
    answer = answer[1:N+1]
    answer.sort(key=lambda x: (-x[0], x[1]))
    
    return [x[1] for x in answer]