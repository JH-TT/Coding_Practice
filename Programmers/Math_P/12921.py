def eratos():
    n = 1000001
    era = [True] * 1000001
    
    for i in range(2, int(n**0.5)+1):
        if era[i]:
            j = 2
            while i * j < n:
                era[i*j] = False
                j += 1
    return era

def solution(n):
    answer = 0
    e = eratos()
    return sum(e[x] for x in range(2, n+1))

# 에라토스테네스의 체를 구현하면 어렵지 않게 푸는 문제