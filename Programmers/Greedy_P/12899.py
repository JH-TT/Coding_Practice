def solution(n):
    arr = ['0', '1', '2', '4']    
    answer = ''
    
    while n > 3:
        a = n % 3
        n //= 3
        if a == 0:
            n -= 1
            a = 3
        answer = arr[a] + answer
    answer = arr[n] + answer
    
    return str(int(answer))

# 나눴을때 나머지가 0이면 몫에서 1을 빼고 나머지를 3으로 지정해 준다.