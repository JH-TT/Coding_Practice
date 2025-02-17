from collections import defaultdict

def solution(n, bans):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    dic = defaultdict(int)
    for i in range(1, len(alpha) + 1):
        dic[alpha[i-1]] = i

    num_bans = []
    for b in bans:
        calc = 0
        for c in range(len(b)):
            calc += dic[b[c]] * (26 ** (len(b) - c - 1))
        num_bans.append(calc)
    num_bans.sort()

    for num in num_bans:
        if num <= n:
            n += 1

    # 여기부터 n값이 최종위치의 알파벳 조합이다.
    cnt = 0
    answer = ""
    while n > 0:
        if n % 26 == 0:
            answer = "z" + answer
            if n == 26:
                break
            n //= 26
            n -= (n % 26 != 0) # 26의 제곱이면 빼지 않는다.
            continue
        answer = alpha[(n % 26) - 1] + answer
        n //= 26

    return answer

# 26진수 느낌으로 풀면 된다.
# 진수랑은 조금 다른 느낌이라 숫자 -> 알파벳 조합으로 변경할때 계산을 잘 해야 한다.