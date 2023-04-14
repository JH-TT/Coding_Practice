def solution(targets):
    answer = 1
    
    targets.sort()
    scope = targets[0]
    for t in targets[1:]:
        if t[0] < scope[1]:
            scope = [max(scope[0], t[0]), min(scope[1], t[1])]
        else:
            scope = t
            answer += 1
    
    return answer

# 일단 범위를 시작부분을 기준으로 정렬한다.
# 첫 범위를 요격 범위로 둔다(그러면 최소 1개이므로 answer는 1로 수정)
# 나머지 target들을 보면서 해당 범위가 현재 요격범위랑 겹치는지 확인한다.
# 만약 겹치면 둘의 공통으로 들어가는 범위를 scope로 지정한다.
# 겹치지 않으면 현재 범위를 scope로 새로 지정하고 answer의 값을 1증가시킨다.