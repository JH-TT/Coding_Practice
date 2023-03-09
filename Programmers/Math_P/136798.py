def solution(number, limit, power):
    divisor = []
    for num in range(1, number+1):
        cnt = countDivisor(num)
        if cnt > limit:
            divisor.append(power)
        else:
            divisor.append(cnt)
    
    return sum(divisor)

def countDivisor(num):
    cnt = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            cnt += 1
    # 일단 약수를 절반까지만 구하고 2배를 곱한다.
    # 만약 n제곱인 경우에는 약수가 홀수개 이니까 그때는 1을 빼준다.
    return cnt * 2 - (num % (num ** (0.5)) == 0)