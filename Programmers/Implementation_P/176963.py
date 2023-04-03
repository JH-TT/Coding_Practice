from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    yearn = defaultdict(int)
    
    for i in range(len(name)):
        yearn[name[i]] = yearning[i]
    
    for p in photo:
        total = 0
        for j in p:
            total += yearn[j]
        answer.append(total)
    
    return answer