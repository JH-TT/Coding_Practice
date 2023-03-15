def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if i % i ** 0.5 == 0:
            answer -= i
        else:
            answer += i
    
    return answer

# 해당 숫자가 n의 제곱 형태면 약수의 개수는 홀수개인것을 이용한 문제이다.
# ex> 16은 4의 제곱이라 약수를 구하면 1, 2, 4, 8, 16 이 된다.
# 약수가 서로 짝을 짓는다는 것을 생각해 보면 바로 떠올릴 수 있다.