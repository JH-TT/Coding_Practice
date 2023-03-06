#풀이 참고
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        # 처음에 이 코드를 추가함으로써 내 코드에서 cnt에 남는 경우를 따로 처리하지 않아도 된다.
        # 애초에 딱 떨어지든 아니든 마지막 부분을 남기는 코드이기 때문에 한번에 처리가 가능하다.
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer

# 내 풀이
def solution(s):
    answer = 0
    cnt = [0, 0]
    target = ""
    
    for i in s:
        if target == "" or target == i:
            target = i
            cnt[0] += 1
        elif target != i:
            cnt[1] += 1
            if cnt[0] == cnt[1]:
                answer += 1
                target = ""
                cnt = [0, 0]
    if cnt != [0, 0]:
        answer += 1
        
    return answer