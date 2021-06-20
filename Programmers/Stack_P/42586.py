def solution(progresses, speeds):
    answer = []
    days = [-((progresses[i] - 100) // speeds[i]) for i in range(len(speeds))] # 각 작업이 100퍼센트가 되려면 며칠걸리는지 저장.(-((progresses[i] - 100) // speeds[i])로 한 이유는 ceil함수를 이용하지 않고 표현하기 위함.)
    # 즉 음수내림 -> 그 음수의 부호를 바꾸면 양수 올림형태.
    # 반복문을 돌면서 앞 작업의 일수가 뒷 작업의 일수보다 많은동안 cnt를 1씩 증가. 아닌 경우 answer에 넣음.
    i = 0
    while i < len(days):
        cnt = 1
        a = days[i]
        while i + 1 < len(days) and a >= days[i + 1]:
            cnt += 1
            i += 1
        answer.append(cnt)
        i += 1
    
    return answer