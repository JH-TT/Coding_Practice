def solution(a, b, n):
    answer = 0
    
    while a <= n:
        cola, rest = divmod(n, a)
        answer += cola * b
        n = rest + cola * b
    
    return answer

# 몫과 나머지를 이용하는 문제
# n이 a보다 작아지면 더이상 교환할 수 없으니 그땐 반복문 종료