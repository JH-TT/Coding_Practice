def solution(n, k):
    answer = 0
    nbits = change_to_nbits(n, k)
    targets = nbits.split("0")
    for t in targets:
        if t == '' or t == '1':
            continue
            
        if check_prime(int(t)):
            answer += 1
    
    return answer

def check_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def change_to_nbits(n, k):
    bit = ''
    while n > 0:
        d, m = divmod(n, k) # 몫, 나머지
        n = d
        bit = str(m) + bit
    
    return bit