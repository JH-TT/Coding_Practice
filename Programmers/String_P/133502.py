def solution(ingredient):
    answer = 0
    ham = ''
    for i in ingredient:
        ham += str(i)
        # in 연산이 느리다보니 사용하면 시간초과가 뜬다. 슬라이싱을 이용했다.
        if '1231' == ham[len(ham)-4:]:
            ham = ham[:len(ham)-4]
            answer += 1
    
    return answer
# replace와 in이 얼마나 느린지 알 수 있었던 문제였다.