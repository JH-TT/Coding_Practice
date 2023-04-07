def solution(plans):
    answer = []
    stop = []
    p = sorted(plans, key = lambda x : x[1]) # 시간순서대로 정렬한다.
    
    for i in range(len(p)-1):
        term = calc_time(p[i][1], p[i+1][1]) # 현재 과제 시작부터 다음 과제까지 남은 시간
        # 만약 현재 과제를 시간안에 충분히 할 수 있으면 answe에 넣는다.
        if int(p[i][2]) <= term:
            term -= int(p[i][2]) # 남은시간
            answer.append(p[i][0])
        # 만약 과제를 시간안에 해결하지 못하면 stop에 남은시간과 넘긴다
        else:
            stop.append([p[i][0], int(p[i][2]) - term])
            continue
        # 시간이 남아있으면 남긴 과제들을 수행한다
        while stop and term > 0:
            t = stop[-1][1] - term # 과제 소요시간 - 남은시간
            # 남은시간안에 과제를 해결하는 경우
            if t <= 0:
                answer.append(stop.pop()[0]) # answer에 넣고
                term = -t # term을 업데이트 해준다
            # 남은시간안에 과제를 해결하지 못하는 경우
            else:
                stop[-1][1] -= term # 과제의 남은 시간을 업데이트하고
                break # 반복문을 끝낸다
        
    answer.append(p[-1][0]) # 가장 늦게 시작한 과제는 남은 과제들보다 먼저 끝난다.
    # 남은 과제들은 순서대로 마친다
    while stop:
        answer.append(stop.pop()[0])
    
    return answer
  
# 두 시간의 차이를 분(minute)으로 계산
def calc_time(a, b):
    a = list(map(int, a.split(":")))
    b = list(map(int, b.split(":")))
    return (b[0]*60+b[1]) - (a[0]*60+a[1])

# 문제에 주어진 과정 그대로 구현하면 되는 문제였다