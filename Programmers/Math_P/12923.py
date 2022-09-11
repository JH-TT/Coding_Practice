def solution(begin, end):
    answer = []
    
    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
            continue
        num = 1
        # 2부터 for문 돌면서 최대 약수를 구한다.
        # 만약 num이 그대로면 그 숫자는 소수가 된다. 그러니 1을 append
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0 and i // j <= 10000000:
                num = i // j
                break
        answer.append(num)
    
    return answer

# 이 문제의 핵심
# 해당 수의 최대 약수를 넣는 문제.
# 소수면 당연히 1일것이고, 그 외엔 for문을 이용해서 해결.
# 효율성때문에 골치아팠음.