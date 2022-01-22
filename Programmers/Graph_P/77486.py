from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    res = defaultdict(list) # 각 회원마다 받은 돈.
    parent = defaultdict(str) # 각 회원의 추천인
    
    for i in range(len(enroll)):         
        parent[enroll[i]] = referral[i]
        res[enroll[i]].append(0)
    
    for i in range(len(seller)):
        s = seller[i]
        a = amount[i] * 100        
        while s != "-":
            dis = a // 10
            if dis < 1:
                res[s].append(a)
                break
            else:
                res[s].append(a - dis)
            s = parent[s]
            a = dis
    for i in range(len(enroll)):
        answer.append(sum(res[enroll[i]]))
    
    return answer