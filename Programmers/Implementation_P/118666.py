def solution(survey, choices):
    answer = ''
    # 성격유형 개수가 많지 않으니 하드코딩으로 직접 초기화 한다.
    s = dict({"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0})

    # 점수를 보면 4번 기준으로 나눴기 때문에 4번은 그냥 넘기고 다른 번호는 4로부터 떨어진 거리가 점수가 된다.
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        if choices[i] < 4:
            s[survey[i][0]] += abs(choices[i] - 4)
        else:
            s[survey[i][1]] += abs(choices[i] - 4)
            
    answer += check_point("RT", s)
    answer += check_point("CF", s)
    answer += check_point("JM", s)
    answer += check_point("AN", s)
        
    return answer

# 해당 지표 번호에서 더 큰 점수를 가진 유형을 선택한다.
# 단 점수가 같으면 사전순이기 때문에 크거나 같다(>=)로 비교한다.
def check_point(t, s):
    if s[t[0]] >= s[t[1]]:
        return t[0]
    return t[1]