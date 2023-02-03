def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    n = len(alpha)
    
    for word in s:
        cnt = 0
        idx = alpha.index(word)
        while cnt < index:
            idx += 1
            if alpha[idx % n] not in skip:
                cnt += 1
        
        answer += alpha[idx % n]
    
    return answer
# 먼저 인덱스를 1증가시키고 그 위치의 알파벳이 skip에 있는지 확인을 하는 순서여야 한다.
# 만약 skip을 먼저 확인하면 마지막 cnt를 증가시키고 while문을 나가야 하는데 인덱스를 1증가시키고 나가게되어 안맞을 수 있다.