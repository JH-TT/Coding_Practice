def solution(cards1, cards2, goal):
    for g in goal:
        # 조건문을 이용해서 해당 조건이 맞으면 pop을 진행하고 아무것도 맞지 않게 되면 No를 리턴한다.
        if cards1 and cards1[0] == g:
            cards1.pop(0)
        elif cards2 and cards2[0] == g:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"