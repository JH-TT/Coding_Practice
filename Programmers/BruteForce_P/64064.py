from collections import defaultdict
from itertools import product

def solution(user_id, banned_id):
    # ban당한 아이디인지 확인
    def match_id(a, b):
        if len(a) != len(b):
            return False
        else:
            for i in range(len(a)):
                if b[i] == "*":
                    continue
                if a[i] != b[i]:
                    return False
        return True    
    # 각 불량사용자 경우에 맞는 유저들
    proper_id = defaultdict(list)

    # 가려진 부분을 제외한 나머지 부분이 일치하는 유저들 맞게 넣는 코드.
    for i in set(banned_id):
        for j in user_id:
            if match_id(j, i):
                proper_id[i].append(j)
    arr = [] # 모든 불량 사용자 유력후보들 넣는곳
    for i in banned_id:
        arr.append(proper_id[i])

    # 모든 경우
    all_case = product(*arr)
    real_case = []
    for i in all_case:
        # 중복되는 아이디가 없는 경우
        if len(i) == len(set(i)):
            # 순서가 달라도 유저목록의 내용이 동일하면 같은 것으로 처리하기 위함.
            sort_case = sorted(list(i))
            # 이미 같은 유저 목록이 있는지 확인
            # 없으면 추가
            if sort_case not in real_case:
                real_case.append(sort_case)
                        
    return len(real_case)