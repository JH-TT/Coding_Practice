# 짝수일땐 // 2
# 홀수일땐 -1
def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans

# binary로 해결한 문제
def solution(n):
    return bin(n).count('1')

# 해당 숫자를 2진수로 표현하면 0과 1로 이뤄져 있는데, 거기에 1의 개수들이 결국 점프하는 개수이다.
# 110이면 right shift는 건전지 사용량이 줄어들지 않지만 011에서 가장 맨앞 1은 홀수라서 1을 빼준다.
# 010에서 또 right shift를해서 001이되고 똑같이 1을 빼면 결국 0이 된다. 이는 결국 1의 개수를 의미하므로 count함수로 처리가 가능하다.