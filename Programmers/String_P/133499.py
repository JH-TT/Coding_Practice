def solution(babbling):
    answer = 0
    bab = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in bab:
            if j*2 not in i:
                i = i.replace(j, ' ')
        if i.strip() == '':
            answer += 1
    
    return answer

# replace를 잘 활용해야헀던 문제