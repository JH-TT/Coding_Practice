def solution(order):
    answer = 0
    sub_container = []
    
    num = 1
    for o in order:
        while num < o:
            sub_container.append(num)
            num += 1
        if num == o:
            answer += 1
            num += 1
        elif sub_container[-1] == o:
            answer += 1
            sub_container.pop()
        else:
            break
    
    return answer

# 큐와 스택을 둘 다 사용해서 푸는 문제...
# 여기서 함정은 둘 다 숫자를 못꺼내는 상황이면 break로 빠져나와야함