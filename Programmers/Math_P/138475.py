from collections import defaultdict

def solution(e, starts):
    answer = []
    cnt = [0] * (e + 1)
    all_case = set()
    d = defaultdict(list)
    
    for i in range(1, e+1):
        for j in range(i, e+1, i):
            cnt[j] += 1
        
    for i in range(e+1):
        all_case.add(cnt[i])
        d[cnt[i]].append(i)
        
    all_case = sorted(all_case, key=lambda x : -x)
    
    for s in starts:
        for a in all_case:
            flag = False
            for b in d[a]:
                if s <= b <= e:
                    answer.append(b)
                    flag = True
                    break
            if flag:
                break
    
    return answer

# e까지 각 약수를 구한 뒤, 구현해서 처리한다. 