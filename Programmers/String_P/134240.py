def solution(food):
    p = ""
    for i, v in enumerate(food[1:]):
        p += str(i+1) * (v // 2)
    
    return p + "0" + p[::-1]

# enumerate를 상기시킨 문제