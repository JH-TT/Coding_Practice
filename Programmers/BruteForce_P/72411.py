from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    
    # a : 확인할 메뉴, b : 비교 대상
    # a문자열들이 b에 다 속해있는지 판단.
    def check_str(a, b):
        for i in a:
            if i not in b:
                return False
        return True
    
    # a : 확인할 메뉴
    # 코스들을 확인하는 함수
    def check_course(a, cnt):
        for order in orders:
            if check_str(a, order):
                cnt += 1 # a가 order안에 있으면 cnt 1 증가
        
        return [cnt, a]
                
    answer = []

    # "WX", "XW"처럼 순서만 다른 애들이 있으니 전부 오름차순으로 통일시킨다.
    a = set()
    for i in orders:
        b = list(i)
        b.sort()
        a.add("".join(b))
    a = list(a)
    
    for i in course:
        sub = set() # i코스들의 집합.
        case = [] # [개수, 문자열]의 형태로 이중리스트가 될 예정
        for j in a:
            if len(j) < i: # 길이가 안되면 다음으로 넘김.
                continue
            for h in list(combinations(j, i)): # 조합을 이용해서 i개를 꺼내는 모든 경우의 수를 확인한다.
                sub.add("".join(h)) # 중복은 없애주기 위해 set으로 이용
        # 개수 확인하는 코드
        for k in sub:
            case.append(check_course(k, 0))
        # 비어있으면 다음으로 넘김.
        if not case:
            continue
        case.sort() # 개수기준으로 정렬
        max_length = case[-1][0] # 가장 많이 등장한 횟수
        for i in case:
            # 2번이상 나왔으며 가장 많이 등장한 메뉴들을 answer에 넣어준다.
            if max_length >= 2 and i[0] == max_length:
                answer.append(i[1])
            
    answer.sort() # 알파벳 순으로 정렬
    
    return answer